import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.endpoints import documents, chat, quiz, summary

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.9.0",
    description="StudyBuddy RAG: Strictly Grounded Study Assistant & Quiz Engine"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router, prefix=f"{settings.API_V1_STR}/documents", tags=["Documents"])
app.include_router(chat.router, prefix=f"{settings.API_V1_STR}/chat", tags=["Chat"])
app.include_router(quiz.router, prefix=f"{settings.API_V1_STR}/quiz", tags=["Quiz"])
app.include_router(summary.router, prefix=f"{settings.API_V1_STR}/summary", tags=["Summary"])

static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/api/health")
def health():
    return {"status": "healthy", "service": settings.PROJECT_NAME, "version": "0.9.0"}

@app.get("/")
def serve_index():
    index_file = os.path.join(static_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "StudyBuddy RAG API Running. Visit /docs for OpenAPI documentation."}
