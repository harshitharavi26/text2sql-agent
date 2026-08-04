from agents.state import SQLAgentState

from prompts.explanation_prompt import (
    build_explanation_prompt
)

from models.llm import generate_response


def generate_answer_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Generate a natural language explanation
    from query results.
    """

    question = state["question"]

    columns = state["columns"]

    rows = state["rows"]


    prompt = build_explanation_prompt(
        question,
        columns,
        rows
    )


    answer = generate_response(prompt)


    return {
        **state,
        "answer": answer.strip()
    }