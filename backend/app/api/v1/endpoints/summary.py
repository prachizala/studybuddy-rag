from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Document, DocumentChunk
from app.services.summary_service import generate_summary

router = APIRouter()

@router.get("/generate/{document_id}")
def get_summary(document_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    chunks = db.query(DocumentChunk).filter(DocumentChunk.document_id == document_id).all()
    text = " ".join([c.text_content for c in chunks])
    return generate_summary(doc.filename, text)
