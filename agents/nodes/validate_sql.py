from agents.state import SQLAgentState

from utils.sql_validator import validate_sql


def validate_sql_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Validate generated SQL.

    Stores:
    - cleaned SQL if valid
    - error message if invalid
    """

    sql = state["sql"]

    is_valid, result = validate_sql(sql)

    if is_valid:

        return {
            **state,
            "sql": result,
            "error": "",
        }

    else:

        return {
            **state,
            "error": result,
        }