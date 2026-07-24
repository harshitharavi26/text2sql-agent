
def build_explanation_prompt(question: str, results) -> str:
    """
    Build a prompt for explaining SQL query results.
    """

    return f"""
You are a data analyst.

A user asked:

{question}

The SQL query returned these results:

{results}

Write a short, clear explanation.

Do not mention SQL.
Keep it under 100 words.
"""