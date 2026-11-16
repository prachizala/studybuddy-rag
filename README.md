# StudyBuddy RAG: Strictly Grounded Study Assistant & Quiz Engine (Prototype)

> **Note:** This early RAG prototype has been superseded by our comprehensive academic intelligence platform [Ai_Notes_Rating_System](https://github.com/prachizala/Ai_Notes_Rating_System) and [Enterprise Knowledge Copilot](https://github.com/prachizala/enterprise-knowledge-copilot). Maintained as a lightweight reference.

[![StudyBuddy RAG CI](https://github.com/prachizala/studybuddy-rag/actions/workflows/ci.yml/badge.svg)](https://github.com/prachizala/studybuddy-rag/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

StudyBuddy RAG is an academic document intelligence portal engineered around strict anti-hallucination retrieval-augmented generation. It parses student textbook PDFs and lecture notes, answers questions solely using verified source passages with page citations, generates active recall quizzes, and produces executive summaries.

---

## Key Features

1. **Strictly Grounded RAG Chat**:
   - Zero-hallucination guardrail: if requested information is absent from ingested notes, the engine explicitly responds: *"The uploaded material does not contain this information."*
   - Transparent citation chips linking every response claim to exact page numbers and chunk excerpts.
2. **5-Question Active Recall Quiz Generator**:
   - Synthesizes multiple-choice questions with real-time feedback, explanatory rationales, and textbook page references.
3. **Executive Summary Mode**:
   - One-click extraction of Core Concepts, Key Definitions, and Revision Takeaways.
4. **Universal Provider-Agnostic LLM Client**:
   - Operates with Gemini API, OpenAI-compatible endpoints, or deterministic offline local mock fallback.

---

## API Endpoints Table

Base URL: `http://localhost:8000`

| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---:|
| `GET` | `/api/health` | Health check and service metadata | No |
| `POST` | `/api/v1/seed` | Seed realistic demo documents, chunks & quizzes | No |
| `GET` | `/api/v1/documents/` | List all ingested academic PDF documents | No |
| `POST` | `/api/v1/documents/upload` | Upload PDF and perform semantic chunking | No |
| `POST` | `/api/v1/chat/query` | Ask a question against ingested document context | No |
| `POST` | `/api/v1/quiz/generate` | Generate active-recall 5-question MCQ quiz | No |
| `POST` | `/api/v1/summary/generate` | Generate executive conceptual revision summary | No |

---

## Quickstart Guide

### 1. Environment Setup
```bash
cd studybuddy-rag
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install --upgrade pip
pip install -r backend/requirements.txt
```

### 2. Populate Demo Data
```bash
python backend/seed_data.py
```

### 3. Run Server
```bash
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
Open `http://localhost:8000` to interact with the RAG workspace, or `http://localhost:8000/docs` for the interactive OpenAPI documentation.

### 4. Run Pytest Suite
```bash
pytest backend/tests/test_rag.py -v
```

---

## Flagship Supersession Notice
This repository is retained as an architectural lightweight reference for deterministic chunking and strict retrieval grounding. For production academic intelligence and enterprise search systems, explore:
- **[Ai_Notes_Rating_System](https://github.com/prachizala/Ai_Notes_Rating_System)**: Comprehensive academic notes evaluation, multi-attribute scoring, and automated feedback suite.
- **[Enterprise Knowledge Copilot](https://github.com/prachizala/enterprise-knowledge-copilot)**: Hybrid dense/sparse vector retrieval with reranking, cross-encoder scoring, and citation provenance.

---

## Author & License
- **Author:** Prachi Zala ([prachizala](https://github.com/prachizala))
- **Email:** prachizala2003@gmail.com
- **License:** MIT License. See [LICENSE](LICENSE) for details.
