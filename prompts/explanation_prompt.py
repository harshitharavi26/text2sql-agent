def build_explanation_prompt(
    question: str,
    columns,
    rows
) -> str:
    """
    Build a prompt for explaining SQL query results.
    """

    return f"""
You are a data analyst.

A user asked:

{question}

The query returned:

Columns:
{columns}

Rows:
{rows}

Write a short, clear explanation.

Rules:
- Do not mention SQL.
- Do not use Markdown.
- Do not use bullet points.
- Do not use mathematical formatting.
- Keep currency values in normal format like $124,191.82.
- Keep the answer under 100 words.
"""