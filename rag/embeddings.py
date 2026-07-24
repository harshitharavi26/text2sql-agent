import ollama

EMBEDDING_MODEL = "nomic-embed-text"


def get_embedding(text: str) -> list[float]:
    """
    Generate an embedding for the given text.
    """

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]