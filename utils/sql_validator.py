FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE"
}



def validate_sql(sql: str) -> bool:
    """
    Validate that the generated SQL is safe to execute.
    """

    sql_upper = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            return False

    return True