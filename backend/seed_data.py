import json
from app.core.database import SessionLocal, Base, engine
from app.models.models import Document, DocumentChunk, ChatSession
from app.services.rag_engine import compute_sparse_embedding

Base.metadata.create_all(bind=engine)
db = SessionLocal()

print("Seeding StudyBuddy RAG database...")

doc = db.query(Document).filter(Document.filename == "BCA_OS_Networking_MasterNotes.pdf").first()
if not doc:
    doc = Document(
        filename="BCA_OS_Networking_MasterNotes.pdf",
        file_size=184200,
        total_pages=3,
        chunk_count=3
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    chunks_data = [
        (1, "An Operating System Kernel manages CPU scheduling, physical RAM allocation, and hardware device communication. It provides abstraction layers for user applications, enforcing memory isolation to prevent crashed processes from corrupting the entire system."),
        (2, "Virtual Memory allows systems to execute processes larger than physical RAM by paging data between disk and memory. CPU scheduling algorithms like Shortest Job First minimize average waiting time, while Round Robin provides equal time quantums to prevent starvation."),
        (3, "The OSI 7-layer reference model organizes network communication. Layer 3 (Network Layer) performs IP addressing and packet routing across networks. Layer 4 (Transport Layer, including TCP) provides reliable connection-oriented delivery with sliding-window congestion control.")
    ]

    for page, text in chunks_data:
        emb = compute_sparse_embedding(text)
        chunk = DocumentChunk(
            document_id=doc.id,
            page_number=page,
            chunk_index=page - 1,
            text_content=text,
            embedding_json=json.dumps(emb)
        )
        db.add(chunk)

    session = ChatSession(id=1, document_id=doc.id, title="OS & Networking Prep")
    db.add(session)
    db.commit()

print("StudyBuddy RAG seeded successfully!")
