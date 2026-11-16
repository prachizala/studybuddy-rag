# Changes Log - StudyBuddy RAG

## Work Package 5: Boilerplate Repos and Profile Review

### Summary of Changes
1. **README.md Supersession & Reference Notice**:
   - Added prominent note at the very top of `README.md`:
     `> **Note:** This early RAG prototype has been superseded by our comprehensive academic intelligence platform [NoteIQ (Ai_Notes_Rating_System)](https://github.com/prachizala/Ai_Notes_Rating_System) and [Enterprise Knowledge Copilot](https://github.com/prachizala/enterprise-knowledge-copilot). Maintained as a lightweight reference.`
   - Documented core anti-hallucination guardrails, sparse embedding retrieval mechanisms, active-recall quiz generator, executive summary extraction, API endpoints table, and local setup guide.
2. **CI & Pytest Configuration**:
   - Added `pytest.ini` with `pythonpath = backend` for seamless root-level pytest execution.
   - Refined `.github/workflows/ci.yml` to trigger on `push` (including `review-fixes`) and `pull_request`.
3. **Verification & Tests**:
   - Ran `pytest backend/tests/test_rag.py` locally: 7 passed out of 7 tests.

### Items Skipped & Rationale
- **Repository Deletion**: Did NOT delete the repository per explicit instructions. The codebase is preserved intact as a reference prototype for grounded document retrieval algorithms.

### Recommendations for Prachi
- **Archive on GitHub**: It is strongly recommended to navigate to **GitHub Repository Settings > Danger Zone > Archive this repository** and mark `studybuddy-rag` as **Archived (Read-Only)**.
  - *Rationale*: Marking this prototype repository as archived clarifies for recruiters and visitors that your active flagship academic AI platform is `Ai_Notes_Rating_System` (NoteIQ) and enterprise retrieval platform is `enterprise-knowledge-copilot`, preventing profile clutter and redundant repository confusion.
