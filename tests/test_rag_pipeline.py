from rag.vector_store import get_schema_context

from prompts.sql_prompt import build_prompt

from models.llm import generate_response


def main():

    question = "Show average salary by department"

    schema_context = get_schema_context(question)

    print("Retrieved Schema")
    print("=" * 50)
    print(schema_context)

    prompt = build_prompt(
        question,
        schema_context
    )

    sql = generate_response(prompt)

    print("\nGenerated SQL")
    print("=" * 50)
    print(sql)


if __name__ == "__main__":
    main()