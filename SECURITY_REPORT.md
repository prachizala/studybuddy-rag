# Security Report: StudyBuddy RAG
- **File Ingestion Sanitization**: File uploads are restricted in size and checked for path traversal.
- **Strict Grounding Safety**: Prompt injection attacks attempting to force general web knowledge are neutralized by the system guardrail.
- **Zero API Key Exposure**: All provider keys reside in `.env` and are never serialized to the client.
