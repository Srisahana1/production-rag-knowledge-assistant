from langchain_ollama import ChatOllama


LLM_MODEL = "llama3.2"


def build_context(documents):
    """
    Combine reranked document chunks with numbered source labels.
    """
    context_parts = []

    for index, document in enumerate(documents, start=1):
        context_parts.append(
            f"[Source {index}]\n{document.page_content}"
        )

    return "\n\n".join(context_parts)


def build_prompt(query: str, documents):
    """
    Build a citation-grounded RAG prompt.
    """
    context = build_context(documents)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using only the context provided below.

Cite the supporting source using [Source 1], [Source 2], etc.
Do not cite a source unless it supports the statement.

If the answer is not available in the context, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt.strip()


def generate_answer(query: str, documents):
    """
    Generate a grounded answer with source citations using Ollama.
    """
    prompt = build_prompt(query, documents)

    llm = ChatOllama(
        model=LLM_MODEL,
        temperature=0,
    )

    response = llm.invoke(prompt)

    return response.content