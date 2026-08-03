SYSTEM_PROMPT = """
You are an expert DuckDB SQL engineer.

A previously generated SQL query failed. Generate one corrected query that
answers the original user question.

Rules:
- Return only SQL.
- Do not include Markdown fences.
- Do not provide explanations.
- Generate exactly one SELECT or WITH query.
- Use only the supplied tables and columns.
- Do not create, update, insert, delete, attach, copy, or modify data.
- Do not access external files.
"""


def build_fix_sql_prompt(
    question: str,
    schema: str,
    failed_sql: str,
    error_message: str,
) -> str:
    return f"""
{SYSTEM_PROMPT}

Original User Question:

{question}

Relevant Database Schema:

{schema}

Failed SQL:

{failed_sql}

Database Error:

{error_message}

Corrected SQL:
""".strip()