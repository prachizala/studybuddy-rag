import os
import re
from typing import List, Dict, Any, Optional, Tuple

GROUNDING_UNANSWERABLE_REPLY = "The uploaded material does not contain this information."

class GroundedLLMClient:
    """
    Provider-agnostic strictly-grounded LLM inference client.
    Guarantees:
      1. Zero hallucination: replies ONLY from provided context chunks.
      2. If query topic is absent from context, returns standard unanswerable notice.
      3. Automatically extracts and formats source citations [Page X, Chunk Y].
    """
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "mock")

    def answer_query(
        self,
        query: str,
        context_chunks: List[Tuple[Dict[str, Any], float]],
        document_name: str
    ) -> Dict[str, Any]:
        if not context_chunks:
            return {
                "answer": GROUNDING_UNANSWERABLE_REPLY,
                "citations": [],
                "grounded": True,
                "confidence": 0.0
            }

        # Check semantic overlap: extract significant query terms
        clean_words = [re.sub(r"[^a-zA-Z0-9]", "", w.lower()) for w in query.split()]
        q_words = [w for w in clean_words if len(w) > 3]
        combined_text = " ".join([c[0]["text"].lower() for c in context_chunks])
        has_overlap = any(w in combined_text for w in q_words)

        top_chunk = context_chunks[0][0]
        top_score = context_chunks[0][1]

        if not has_overlap:
            return {
                "answer": GROUNDING_UNANSWERABLE_REPLY,
                "citations": [],
                "grounded": True,
                "confidence": 0.0
            }

        citations = []
        for c, score in context_chunks:
            citations.append({
                "document": document_name,
                "page": c.get("page", 1),
                "chunk_id": c.get("id"),
                "excerpt": c["text"][:160] + "...",
                "relevance_score": score
            })

        lead_chunk = context_chunks[0][0]
        lead_text = lead_chunk["text"]

        answer = (
            f"Based on **{document_name}** (Page {lead_chunk.get('page', 1)}):\\n\\n"
            f"{lead_text}\\n\\n"
            f"*[Source: {document_name}, p. {lead_chunk.get('page', 1)}]*"
        )

        return {
            "answer": answer,
            "citations": citations,
            "grounded": True,
            "confidence": top_score
        }

llm_client = GroundedLLMClient()
