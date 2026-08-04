from rag.vector_store import search_schema

from agents.state import SQLAgentState


def retrieve_schema_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Retrieve relevant database schema using ChromaDB RAG.
    """

    question = state["question"]

    results = search_schema(question)

    documents = results.get(
        "documents",
        [[]]
    )[0]

    if not documents:
        return {
            **state,
            "schema": "",
            "error": "No relevant schema found."
        }

    schema = "\n\n".join(documents)

    return {
        **state,
        "schema": schema,
    }