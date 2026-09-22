from .config import TOP_K


def retrieve_documents(vector_store, query: str, top_k: int = TOP_K):
    """
    Retrieve the most relevant document chunks for a user query.
    """
    documents = vector_store.similarity_search(
        query=query,
        k=top_k,
    )

    return documents