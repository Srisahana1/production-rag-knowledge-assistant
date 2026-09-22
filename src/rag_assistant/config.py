from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
SAMPLE_DATA_DIR = DATA_DIR / "sample"

# Vector database directory
CHROMA_DIR = BASE_DIR / "chroma_db"

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# RAG settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 5

# ChromaDB collection
COLLECTION_NAME = "rag_documents"