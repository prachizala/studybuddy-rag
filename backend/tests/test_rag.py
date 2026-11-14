import pytest
from app.services.rag_engine import chunk_text, compute_sparse_embedding, cosine_similarity, retrieve_top_k_chunks
from app.services.llm_client import llm_client, GROUNDING_UNANSWERABLE_REPLY

def test_semantic_chunking():
    sample = "Word " * 200
    chunks = chunk_text(sample, chunk_size=50, overlap=10)
    assert len(chunks) >= 4
    assert len(chunks[0].split()) <= 50

def test_sparse_embedding_and_similarity():
    v1 = compute_sparse_embedding("Operating system kernel memory management")
    v2 = compute_sparse_embedding("Operating system kernel memory management")
    v3 = compute_sparse_embedding("French culinary recipes and baking techniques")

    assert len(v1) == 256
    sim_identical = cosine_similarity(v1, v2)
    sim_different = cosine_similarity(v1, v3)

    assert sim_identical >= 0.99
    assert sim_different < 0.40

def test_strict_grounding_anti_hallucination():
    # Context about computer science
    chunks = [
        ({"id": 1, "page": 1, "text": "Operating system kernels manage memory and CPU arbitration."}, 0.45)
    ]

    # Query within context
    ans_valid = llm_client.answer_query("What does an OS kernel manage?", chunks, "Notes.pdf")
    assert ans_valid["grounded"] is True
    assert len(ans_valid["citations"]) > 0

    # Query COMPLETELY absent from context (should refuse)
    ans_absent = llm_client.answer_query("Who won the 1998 FIFA World Cup final in Paris?", chunks, "Notes.pdf")
    assert ans_absent["answer"] == GROUNDING_UNANSWERABLE_REPLY
    assert len(ans_absent["citations"]) == 0


def test_pdf_upload_stream_extraction():
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 50), "Distributed systems achieve high availability through replication.")
    pdf_bytes = doc.write()
    doc.close()

    # Verify fitz stream reading
    opened = fitz.open(stream=pdf_bytes, filetype="pdf")
    extracted = opened[0].get_text()
    opened.close()

    assert "replication" in extracted
    assert len(extracted) > 20
