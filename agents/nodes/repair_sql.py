from agents.state import SQLAgentState

from agents.sql_repair import repair_sql


def repair_sql_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Repair failed SQL using LLM.
    """

    question = state["question"]

    schema = state["schema"]

    failed_sql = state["sql"]

    error_message = state["error"]


    repaired_sql = repair_sql(
        question,
        schema,
        failed_sql,
        error_message,
    )


    return {
        **state,
        "repaired_sql": repaired_sql,
        "sql": repaired_sql,
        "repaired": True,
        "error": "",
    }