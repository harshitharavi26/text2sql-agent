from rag.vector_store import search_schema
from prompts.sql_prompt import build_prompt
from models.llm import generate_response
from database.query_executor import execute_query
from agents.sql_repair import repair_sql
from agents.explanation_agent import generate_answer
from utils.sql_validator import validate_sql


def answer_question(question):

    # Retrieve schema
    results = search_schema(question)
    documents = results.get("documents", [[]])[0]

    if not documents:
        return {
        "success": False,
        "repaired": False,
        "error": "No relevant schema found.",
    }

    schema = "\n\n".join(documents)

    # Generate SQL
    prompt = build_prompt(question, schema)
    original_sql = generate_response(prompt).strip()

    # Validate original SQL
    is_valid, validation_result = validate_sql(original_sql)

    if is_valid:
        original_sql = validation_result
        columns, rows = execute_query(original_sql)
    else:
        columns = None
        rows = validation_result

    # Original SQL worked
    if columns is not None:

        answer = generate_answer(
            question,
            columns,
            rows
        )

        return {
            "success": True,
            "repaired": False,
            "schema": schema,
            "sql": original_sql,
            "columns": columns,
            "rows": rows,
            "answer": answer,
        }

    # Original SQL failed
    original_error = rows

    # Repair SQL
    repaired_sql = repair_sql(
        question,
        schema,
        original_sql,
        original_error,
    ).strip()

    # Validate repaired SQL
    is_valid, validation_result = validate_sql(repaired_sql)

    if not is_valid:
        return {
            "success": False,
            "repaired": True,
            "schema": schema,
            "original_sql": original_sql,
            "original_error": original_error,
            "sql": repaired_sql,
            "error": validation_result,
        }

    repaired_sql = validation_result

    # Execute repaired SQL
    columns, rows = execute_query(repaired_sql)

    if columns is not None:

        answer = generate_answer(
            question,
            columns,
            rows
        )

        return {
            "success": True,
            "repaired": True,
            "schema": schema,
            "original_sql": original_sql,
            "original_error": original_error,
            "sql": repaired_sql,
            "columns": columns,
            "rows": rows,
            "answer": answer,
        }

    # Repaired SQL also failed
    return {
        "success": False,
        "repaired": True,
        "schema": schema,
        "original_sql": original_sql,
        "original_error": original_error,
        "sql": repaired_sql,
        "error": rows,
    }