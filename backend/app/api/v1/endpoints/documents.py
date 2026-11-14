import json
import fitz  # PyMuPDF for real binary PDF text extraction
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Document, DocumentChunk
from app.services.rag_engine import chunk_text, compute_sparse_embedding

router = APIRouter()

@router.get("/")
def list_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).order_by(Document.id.desc()).all()
    return [{
        "id": d.id,
        "filename": d.filename,
        "file_size": d.file_size,
        "total_pages": d.total_pages,
        "chunk_count": d.chunk_count,
        "uploaded_at": d.uploaded_at
    } for d in docs]

@router.post("/upload")
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = file.file.read()
    filename = file.filename.lower()
    extracted_pages = []

    # If PDF, parse real pages using PyMuPDF
    if filename.endswith(".pdf"):
        try:
            doc_fitz = fitz.open(stream=content, filetype="pdf")
            for page_idx in range(len(doc_fitz)):
                page = doc_fitz[page_idx]
                text = page.get_text()
                if text.strip():
                    extracted_pages.append((page_idx + 1, text))
            doc_fitz.close()
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Failed to parse PDF document: {str(e)}")
    else:
        # Plaintext or Markdown
        try:
            text = content.decode("utf-8")
            extracted_pages.append((1, text))
        except Exception:
            raise HTTPException(status_code=422, detail="Invalid text file encoding. UTF-8 required.")

    if not extracted_pages:
        raise HTTPException(status_code=400, detail="Document appears to be empty or contains no extractable text.")

    total_chunks = 0
    doc = Document(
        filename=file.filename,
        file_size=len(content),
        total_pages=len(extracted_pages),
        chunk_count=0
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    for page_num, page_text in extracted_pages:
        page_chunks = chunk_text(page_text, chunk_size=300, overlap=50)
        for idx, c_text in enumerate(page_chunks):
            emb = compute_sparse_embedding(c_text)
            chunk_obj = DocumentChunk(
                document_id=doc.id,
                page_number=page_num,
                chunk_index=total_chunks,
                text_content=c_text,
                embedding_json=json.dumps(emb)
            )
            db.add(chunk_obj)
            total_chunks += 1

    doc.chunk_count = total_chunks
    db.commit()

    return {"document_id": doc.id, "filename": doc.filename, "pages": len(extracted_pages), "chunks_indexed": total_chunks}
