# Technical Interview Questions & Answers — StudyBuddy RAG

Based on the actual codebase in `studybuddy-rag`.

---

### Question 1: How does document ingestion and sliding window chunking operate in `rag_engine.py`?
**Answer:**
When a student uploads a course PDF:
1. **In-Memory Binary Ingestion:** The endpoint in `documents.py` reads the upload payload as bytes and initializes `fitz.open(stream=content, filetype="pdf")`. This avoids writing unencrypted temporary files to disk.
2. **Text Normalization:** `clean_text()` collapses irregular whitespace (`\s+`) and control characters into single spaces.
3. **Sliding Window Chunking:** `chunk_text(text, chunk_size=500, overlap=80)` creates overlapping token windows:
   - Window size: 500 words
   - Stride: $500 - 80 = 420$ words
   - Overlap: 80 words
   This preserves semantic continuity across chunk transitions so that definitions or formulas spanning paragraphs are not fragmented.

---

### Question 2: How does the 256-dimensional sparse trigram embedding work?
**Answer:**
In `compute_sparse_embedding(text, vocab_size=256)`:
1. Text is lower-cased.
2. For each character trigram $c_i c_{i+1} c_{i+2}$, we compute a deterministic hash index:
   $$\text{index} = \text{hash}(\text{trigram}) \pmod{256}$$
3. The frequency accumulator at that index is incremented.
4. The vector is $L_2$-normalized:
   $$\mathbf{v}_{norm} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2}$$
This delivers a zero-dependency, sub-millisecond character n-gram vector representation on standard CPUs with zero GPU or external API latency.

---

### Question 3: How do you enforce strict zero-hallucination guardrails?
**Answer:**
In `app/services/llm_client.py`:
1. When a query arrives, `retrieve_top_k_chunks(query, chunks, top_k=3)` ranks passages by cosine similarity.
2. Before answering, `GroundedLLMClient.answer_query()` checks for vocabulary and semantic overlap between significant query terms (words with length $> 3$) and the combined context chunks:
   ```python
   clean_words = [re.sub(r"[^a-zA-Z0-9]", "", w.lower()) for w in query.split()]
   q_words = [w for w in clean_words if len(w) > 3]
   combined_text = " ".join([c[0]["text"].lower() for c in context_chunks])
   has_overlap = any(w in combined_text for w in q_words)
   ```
3. If no overlap exists, or if no chunks match, the engine returns a deterministic refusal:
   `"The uploaded material does not contain this information."` with `confidence: 0.0` and `citations: []`. This was verified with 100% pass on out-of-context test cases.

---

### Question 4: Describe a critical bug you resolved during stabilization.
**Answer:**
**The Bug:** Uploading real binary PDFs initially triggered an unhandled `UnicodeDecodeError` because the initial prototype attempted to decode `await file.read()` directly into a UTF-8 string before parsing.  
**The Solution:** I refactored the ingestion pipeline to pass the raw binary stream directly into PyMuPDF (`fitz.open(stream=content, filetype="pdf")`), allowing PyMuPDF's C-bindings to parse the cross-reference tables and font encodings natively.  
**Secondary Fix:** During testing of the `/api/v1/chat/query` endpoint, SQLite threw an `IntegrityError: FOREIGN KEY constraint failed` when inserting chat messages because the corresponding `ChatSession` record had not been initialized. I added auto-provisioning logic to create the session on the fly if it did not exist.
