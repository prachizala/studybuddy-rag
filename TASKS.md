# Task Management Board (Day 1 - Day 7)
## Project: StudyBuddy RAG

| Task ID | Title / Work Item | Assignee Role | Status | Acceptance Criteria | Branch |
|---|---|---|---|---|---|
| **T-SBR-001** | Day 1 Architecture & Specifications | Architect / PM | Done | PRD, ARCHITECTURE, DESIGN, and TASKS finalized | `docs/T-001-day1-specifications` |
| **T-SBR-002** | Git Repository & CI Base Setup | DevOps Engineer | Done | `.gitignore`, `.env.example`, initial tag v0.1.0 | `chore/T-002-repo-setup` |
| **T-SBR-003** | PDF/Markdown Extraction & Chunking | Backend Engineer | Done | Clean text extraction and recursive sliding chunking engine | `feat/T-003-ingestion-engine` |
| **T-SBR-004** | ChromaDB / Vector Store Integration | AI Engineer | Done | Embedding storage, metadata index, and top-k retrieval | `feat/T-004-chromadb-store` |
| **T-SBR-005** | Universal Provider-Agnostic LLM Client | Backend / AI | Done | Unified client reading from .env with fallback test driver | `feat/T-005-llm-client` |
| **T-SBR-006** | Strictly Grounded RAG Chat Engine | AI Engineer | Done | Grounding prompt, citation extraction, anti-hallucination guard | `feat/T-006-grounded-chat` |
| **T-SBR-007** | Automated Quiz Generation Engine | Backend / AI | Done | MCQ generation from chunks with validated schema output | `feat/T-007-quiz-engine` |
| **T-SBR-008** | Executive Summary Mode Service | Backend / AI | Done | Structured key takeaway and vocabulary synthesis | `feat/T-008-summary-engine` |
| **T-SBR-009** | React Frontend Skeleton & Workspace UI | Frontend Engineer | Done | Split-panel layout, file drag-and-drop, tab navigation | `feat/T-009-frontend-ui` |
| **T-SBR-010** | Citation Inspector & Source Viewer | Frontend Engineer | Done | Clickable citation badges opening source text verification drawer | `feat/T-010-citation-ui` |
| **T-SBR-011** | Grounding & RAG Evaluation Test Suite | QA Engineer | Done | Pytest suite verifying zero hallucination on unanswerable queries | `test/T-011-rag-evaluation` |
| **T-SBR-012** | Security & File Ingestion Hardening | Security Reviewer | Done | Upload sanitize checks, file size caps, no secret leaks | `sec/T-012-security-review` |
| **T-SBR-013** | Docker & Compose Deployment Setup | DevOps Engineer | Done | Multi-container setup with persistent ChromaDB volume | `chore/T-013-docker-setup` |
| **T-SBR-014** | Documentation, Demo Script & v0.9.0 Tag | Technical Writer | Done | README.md, benchmark notes, demo video script | `docs/T-014-final-docs` |
