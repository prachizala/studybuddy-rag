# Product Requirements Document (PRD)
## StudyBuddy RAG: Grounded Study Assistant & Quiz Engine

### 1. Executive Summary & Problem Statement
Students and competitive exam aspirants review massive volumes of academic literature, technical lecture notes, and textbook PDFs. When asking standard commercial AI chatbots for assistance, students frequently encounter hallucinated facts, false historical dates, and fabricated formulas that can result in academic penalties.

**StudyBuddy RAG** solves this with an uncompromising **Strictly Grounded Retrieval-Augmented Generation (RAG)** architecture. It parses uploaded notes and PDFs into ChromaDB vector collections, restricting all generative responses exclusively to user-uploaded context with explicit chunk citations. In addition, it features an automated active-recall Quiz Engine and Executive Summary synthesizer.

---

### 2. User Personas
- **University Student**: Uploads course textbooks and lecture slides to ask granular syllabus questions, verify theorem proofs, and review source citations.
- **Self-Directed Learner**: Uploads technical papers and uses the Quiz Generator to test conceptual retention before exams.
- **Educator / Teaching Assistant**: Uses the Summary Mode to rapidly synthesize lecture notes into executive study outlines and flashcards.

---

### 3. Scope & Prioritization (MoSCoW)
Scope is strictly frozen at the conclusion of Day 1.

#### MUST HAVE (Target MVP - Days 1-5)
- **Document Ingestion Engine**: PDF and Markdown document upload, clean text extraction, recursive semantic chunking (chunk size: 800 tokens, overlap: 100 tokens), and metadata preservation (page number, chunk ID).
- **ChromaDB Vector Store**: Local vector storage with persistent cosine distance embeddings.
- **Provider-Agnostic LLM Connector**: Single standardized client interface (`llm_client.py`) reading API keys from `.env` supporting cloud LLM APIs, OpenAI-compatible endpoints, or local LLMs.
- **Strictly Grounded Chat Assistant**: System prompt engineering enforcing strict anti-hallucination guardrails: if an answer is absent from the uploaded source, the model must explicitly respond: *"The uploaded material does not contain this information."*
- **Verifiable Source Citations**: Every generated response includes expandable citation badges detailing source document name, page number, and literal text chunk snippet.
- **Active Recall Quiz Generator**: Automated generation of 5-question Multiple Choice Quizzes (MCQs) and concept flashcards derived exclusively from selected document chunks, with answer keys and rationale.
- **Executive Summary Engine**: One-click extraction of Core Thesis, Key Definitions, and Practical Takeaways.
- **Session History**: Multi-conversation session management stored locally.

#### SHOULD HAVE (Days 5-6)
- Multi-document comparative search within a single query session.
- Export quiz and summary to Markdown / PDF format.

#### COULD HAVE (Deferred to Post-MVP)
- Spaced-repetition Leitner flashcard practice mode.
- Speech-to-text audio lecture transcription.

#### WON'T HAVE (Out of Scope for 7-Day Sprint)
- Real-time collaborative multi-user study rooms.
- Cloud OCR for handwritten notes (digital text PDFs supported).

---

### 4. Non-Functional Requirements
- **Groundedness Guarantee**: 100% adherence to source boundary in ground-truth evaluation suite.
- **Latency**: Semantic chunk retrieval in under 150ms; first-token streaming response in under 1.5s.
- **Observability**: Transparent chunk similarity scoring displayed in UI debug panel.
