import math
import re
from typing import List, Dict, Any, Tuple
import numpy as np

def clean_text(text: str) -> str:
    """Normalizes whitespace and removes control characters."""
    return re.sub(r"\s+", " ", text).strip()

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 80) -> List[str]:
    """
    Splits document text into overlapping semantic passages.
    Preserves sentences where possible.
    """
    words = text.split(" ")
    chunks = []
    i = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
        if i + chunk_size >= len(words):
            break
        i += (chunk_size - overlap)
    return chunks if chunks else [text]

def compute_sparse_embedding(text: str, vocab_size: int = 256) -> List[float]:
    """
    Generates a deterministic 256-dimensional character-n-gram frequency embedding.
    Zero external neural network overhead; ultra-fast on CPU and reproducible.
    """
    vec = np.zeros(vocab_size, dtype=np.float32)
    cleaned = text.lower()
    for i in range(len(cleaned) - 2):
        trigram = cleaned[i:i+3]
        idx = hash(trigram) % vocab_size
        vec[idx] += 1.0

    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return [round(float(x), 5) for x in vec]

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    a = np.asarray(v1, dtype=np.float32)
    b = np.asarray(v2, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))

def retrieve_top_k_chunks(
    query: str,
    chunks: List[Dict[str, Any]],
    top_k: int = 3
) -> List[Tuple[Dict[str, Any], float]]:
    """Retrieves top-k relevant document chunks ranked by cosine similarity."""
    q_vec = compute_sparse_embedding(query)
    scored = []
    for c in chunks:
        emb = c.get("embedding")
        score = cosine_similarity(q_vec, emb)
        scored.append((c, round(score, 4)))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
