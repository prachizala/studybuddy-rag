import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Document, DocumentChunk, ChatSession, ChatMessage
from app.services.rag_engine import retrieve_top_k_chunks
from app.services.llm_client import llm_client

router = APIRouter()

class QueryRequest(BaseModel):
    document_id: int
    session_id: int = 1
    query: str

@router.post("/query")
def query_rag(req: QueryRequest, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == req.document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # Ensure ChatSession exists (P1 Fix: prevent foreign key failure)
    session_obj = db.query(ChatSession).filter(ChatSession.id == req.session_id).first()
    if not session_obj:
        session_obj = ChatSession(id=req.session_id, document_id=doc.id, title=f"Study Session: {doc.filename}")
        db.add(session_obj)
        db.commit()

    # Load chunks
    chunks_db = db.query(DocumentChunk).filter(DocumentChunk.document_id == req.document_id).all()
    chunk_list = []
    for c in chunks_db:
        chunk_list.append({
            "id": c.id,
            "page": c.page_number,
            "text": c.text_content,
            "embedding": json.loads(c.embedding_json)
        })

    top_chunks = retrieve_top_k_chunks(req.query, chunk_list, top_k=3)
    response = llm_client.answer_query(req.query, top_chunks, doc.filename)

    # Save to session
    msg_user = ChatMessage(session_id=session_obj.id, role="user", content=req.query)
    msg_bot = ChatMessage(
        session_id=session_obj.id,
        role="assistant",
        content=response["answer"],
        citations_json=json.dumps(response.get("citations", []))
    )
    db.add_all([msg_user, msg_bot])
    db.commit()

    return response
