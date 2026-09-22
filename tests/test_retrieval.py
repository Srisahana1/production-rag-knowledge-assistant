from langchain_core.documents import Document

from src.rag_assistant.retrieval import retrieve_documents


class FakeVectorStore:
    def similarity_search(self, query, k):
        return [
            Document(page_content="RAG combines retrieval with generation."),
            Document(page_content="ChromaDB is a vector database."),
        ][:k]


def test_retrieve_documents():
    vector_store = FakeVectorStore()

    results = retrieve_documents(
        vector_store,
        query="What is RAG?",
        top_k=2,
    )

    assert len(results) == 2
    assert "RAG" in results[0].page_content