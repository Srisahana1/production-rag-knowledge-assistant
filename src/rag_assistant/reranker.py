from sentence_transformers import CrossEncoder


RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"


class DocumentReranker:
    """
    Rerank retrieved documents using a CrossEncoder model.
    """

    def __init__(self):
        self.model = CrossEncoder(RERANKER_MODEL)

    def rerank(self, query: str, documents, top_n: int = 3):
        if not documents:
            return []

        pairs = [
            (query, document.page_content)
            for document in documents
        ]

        scores = self.model.predict(pairs)

        ranked_documents = sorted(
            zip(documents, scores),
            key=lambda item: float(item[1]),
            reverse=True,
        )

        return [
            document
            for document, _ in ranked_documents[:top_n]
        ]