# Academic Prompt Engineering & Citation Invariants

## System Objective
Enforces strict citation grounding and eliminates hallucination in academic question-answering.

## Grounding Protocol
1. Every assertion must cite page number and section header `[Source: Doc-A, p.14]`.
2. In-context unanswerable queries must return deterministic fallback: `Insufficient evidence in context.`
