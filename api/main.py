from fastapi import FastAPI
from pydantic import BaseModel

from src.rag_assistant.pipeline import RAGPipeline


app = FastAPI(
    title="Production RAG Knowledge Assistant",
    version="1.0.0",
)


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    """
    Health check endpoint for the API.
    """
    return {"status": "healthy"}


@app.post("/query")
def query_documents(request: QueryRequest):
    """
    Ask a question using the existing RAG knowledge base.
    """
    pipeline = RAGPipeline(load_existing=True)

    result = pipeline.query(request.question)

    sources = [
        {
            "source": index,
            "page": document.metadata.get("page", 0) + 1,
            "file": document.metadata.get("source"),
        }
        for index, document in enumerate(
            result["sources"],
            start=1,
        )
    ]

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": sources,
    }