import re


FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "ATTACH",
    "DETACH",
    "COPY",
    "INSTALL",
    "LOAD",
}


def validate_sql(sql: str):
    """
    Validate that generated SQL is a single read-only query.

    Returns:
        On success:
            True, normalized_sql

        On failure:
            False, error_message
    """

    if not sql or not sql.strip():
        return False, "Generated SQL is empty."

    normalized_sql = sql.strip()

    # Remove Markdown fences sometimes returned by the LLM.
    normalized_sql = re.sub(
        r"^```(?:sql)?\s*",
        "",
        normalized_sql,
        flags=re.IGNORECASE,
    )

    normalized_sql = re.sub(
        r"\s*```$",
        "",
        normalized_sql,
    ).strip()

    # Only read-only query types are allowed.
    if not re.match(
        r"^(SELECT|WITH)\b",
        normalized_sql,
        flags=re.IGNORECASE,
    ):
        return False, "Only SELECT and WITH queries are allowed."

    # Reject forbidden operations using word boundaries.
    for keyword in FORBIDDEN_KEYWORDS:
        pattern = rf"\b{keyword}\b"

        if re.search(
            pattern,
            normalized_sql,
            flags=re.IGNORECASE,
        ):
            return False, (
                f"Forbidden SQL operation detected: {keyword}"
            )

    # Reject multiple SQL statements.
    statements = [
        statement.strip()
        for statement in normalized_sql.split(";")
        if statement.strip()
    ]

    if len(statements) != 1:
        return False, "Only one SQL statement is allowed."

    return True, statements[0]