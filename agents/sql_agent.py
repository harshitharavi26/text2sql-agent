from rag.vector_store import search_schema
from prompts.sql_prompt import build_prompt
from models.llm import generate_response
from database.query_executor import execute_query
from agents.sql_repair import repair_sql


def answer_question(question):
    """
    Run the Text-to-SQL pipeline.

    If the first SQL query fails, repair it and retry once.
    """

    # Retrieve relevant schema
    results = search_schema(question)

    schema = "\n\n".join(results["documents"][0])

    # Generate the initial SQL
    prompt = build_prompt(question, schema)
    original_sql = generate_response(prompt).strip()

    # First execution attempt
    columns, rows = execute_query(original_sql)

    if columns is not None:
        return {
            "success": True,
            "repaired": False,
            "schema": schema,
            "sql": original_sql,
            "columns": columns,
            "rows": rows,
        }

    # Save the first database error
    original_error = rows

    # Ask the repair agent to fix the SQL
    repaired_sql = repair_sql(
        question=question,
        schema=schema,
        failed_sql=original_sql,
        error_message=original_error,
    ).strip()

    # Second execution attempt
    repaired_columns, repaired_rows = execute_query(
        repaired_sql
    )

    if repaired_columns is not None:
        return {
            "success": True,
            "repaired": True,
            "schema": schema,
            "original_sql": original_sql,
            "original_error": original_error,
            "sql": repaired_sql,
            "columns": repaired_columns,
            "rows": repaired_rows,
        }

    # The repaired SQL also failed
    return {
        "success": False,
        "repaired": True,
        "schema": schema,
        "original_sql": original_sql,
        "original_error": original_error,
        "sql": repaired_sql,
        "error": repaired_rows,
    }