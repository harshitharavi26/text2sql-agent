from agents.state import SQLAgentState

from prompts.sql_prompt import build_prompt
from models.llm import generate_response


def generate_sql_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Generate SQL query using retrieved schema
    and user question.
    """

    question = state["question"]

    schema = state["schema"]

    prompt = build_prompt(
        question,
        schema
    )

    sql = generate_response(prompt).strip()

    return {
        **state,
        "sql": sql,
        "original_sql": sql,
    }