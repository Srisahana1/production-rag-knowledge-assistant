from .ingestion import load_pdf
from .chunking import split_documents
from .vector_store import create_vector_store, load_vector_store
from .retrieval import retrieve_documents
from .reranker import DocumentReranker
from .generation import generate_answer


class RAGPipeline:
    """
    End-to-end Retrieval-Augmented Generation pipeline.
    """

    def __init__(self, load_existing: bool = False):
        if load_existing:
            self.vector_store = load_vector_store()
        else:
            self.vector_store = None

        self.reranker = DocumentReranker()

    def ingest(self, file_path: str):
        documents = load_pdf(file_path)
        chunks = split_documents(documents)
        self.vector_store = create_vector_store(chunks)

        return len(chunks)

    def query(self, question: str):
        if self.vector_store is None:
            raise ValueError("No documents have been ingested or loaded.")

        retrieved_documents = retrieve_documents(
            self.vector_store,
            question,
        )

        reranked_documents = self.reranker.rerank(
            question,
            retrieved_documents,
        )

        answer = generate_answer(
            question,
            reranked_documents,
        )

        return {
            "answer": answer,
            "sources": reranked_documents,
        }