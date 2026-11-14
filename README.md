# StudyBuddy RAG: Strictly Grounded Study Assistant & Quiz Engine

StudyBuddy RAG is an academic revision and document intelligence portal engineered around strict anti-hallucination retrieval-augmented generation. It parses student textbook PDFs and notes, answers questions solely using verified source passages with page citations, generates active recall quizzes, and produces executive summaries.

---

## 🌟 Key Features

1. **Strictly Grounded RAG Chat**:
   - Zero hallucination guardrail: if information is absent from notes, model explicitly returns: *"The uploaded material does not contain this information."*
   - Transparent citation chips linking every claim to page number and chunk excerpt.
2. **5-Question Active Recall Quiz Generator**:
   - Generates MCQs with immediate feedback, answer explanations, and syllabus page references.
3. **Executive Summary Mode**:
   - One-click synthesis of Core Concept summaries, Key Definitions, and Revision Takeaways.
4. **Universal Provider-Agnostic LLM Client**:
   - Works seamlessly with LLM API, OpenAI-compatible APIs, or an offline deterministic engine.

---

## 🚀 Quickstart Guide

```bash
cd backend
python seed_data.py
python -m pytest -v tests/
uvicorn app.main:app --reload --port 8000
```
Open `http://localhost:8000` for the interactive RAG workspace.

---

## 👤 Author
**Prachi Zala** | [GitHub](https://github.com/prachizala)
