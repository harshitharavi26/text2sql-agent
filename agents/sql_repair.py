from models.llm import generate_response
from prompts.fix_sql_prompt import build_fix_sql_prompt


def repair_sql(
    question: str,
    schema: str,
    failed_sql: str,
    error_message: str,
) -> str:
    """
    Ask the LLM to repair a failed SQL query using the
    original question, relevant schema, and database error.
    """

    prompt = build_fix_sql_prompt(
        question=question,
        schema=schema,
        failed_sql=failed_sql,
        error_message=error_message,
    )

    repaired_sql = generate_response(prompt)

    return repaired_sql.strip()