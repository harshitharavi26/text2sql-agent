from typing import TypedDict, List, Any


class SQLAgentState(TypedDict):

    question: str

    schema: str

    sql: str

    original_sql: str

    repaired_sql: str

    columns: List[str]

    rows: List[Any]

    answer: str

    error: str

    repaired: bool