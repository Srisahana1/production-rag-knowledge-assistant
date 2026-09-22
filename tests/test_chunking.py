from langchain_core.documents import Document

from src.rag_assistant.chunking import split_documents


def test_split_documents():
    document = Document(
        page_content="Artificial intelligence " * 200
    )

    chunks = split_documents([document])

    assert len(chunks) > 1

    for chunk in chunks:
        assert len(chunk.page_content) <= 1000