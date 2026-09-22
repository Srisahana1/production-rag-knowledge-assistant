from langchain_chroma import Chroma

from .config import CHROMA_DIR, COLLECTION_NAME
from .embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a Chroma vector store from document chunks.
    """
    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )

    return vector_store


def load_vector_store():
    """
    Load the existing persistent Chroma vector store.
    """
    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
    )

    return vector_store