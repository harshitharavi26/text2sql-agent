from agents.state import SQLAgentState

from database.query_executor import execute_query


def execute_sql_node(
    state: SQLAgentState
) -> SQLAgentState:
    """
    Execute validated SQL query.

    Stores:
    - columns
    - rows

    If execution fails:
    - stores error
    """

    sql = state["sql"]

    columns, rows = execute_query(sql)

    if columns is None:

        return {
            **state,
            "error": rows,
        }

    return {
        **state,
        "columns": columns,
        "rows": rows,
        "error": "",
    }