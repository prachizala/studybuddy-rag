# StudyBuddy RAG: 3-Minute Video Demo Script

**Speaker**: Prachi Zala  
**Target Audience**: Technical Recruiters, Examiners, Academic Mentors  

### [00:00 - 00:30] The Hallucination Problem in Study AI
"Hello! I'm Prachi Zala. When students use standard commercial chatbots or commercial LLMs to study, the models frequently hallucinate incorrect dates, formulas, or theorems not in their course syllabus. StudyBuddy RAG solves this through strictly grounded retrieval with zero tolerance for hallucinations."

### [00:30 - 01:30] Grounded Q&A & Verifiable Citations
"I've uploaded my Operating Systems notes. When I ask 'What is the role of an OS kernel?', notice how StudyBuddy answers exclusively from Page 1, attaching a clickable citation badge. If I test its anti-hallucination guard by asking an out-of-domain question like 'Who won the 1998 World Cup?', it strictly refuses: 'The uploaded material does not contain this information.'"

### [01:30 - 02:30] Quiz Engine & Executive Summary
"StudyBuddy also features an active recall quiz generator. With one click, it synthesizes five Multiple Choice Questions complete with answer keys and page references. Our summary mode condenses 50 pages into high-yield definitions."

### [02:30 - 03:00] Stack & Architecture
"Built with FastAPI, NumPy vector embeddings, PyMuPDF, and a provider-agnostic LLM interface, fully tested with pytest and ready for deployment. Thank you!"
