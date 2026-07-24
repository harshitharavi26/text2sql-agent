from prompts.sql_prompt import build_sql_prompt
from models.llm import generate_response
from database.db import execute_query
from utils.sql_validator import validate_sql
from prompts.explanation_prompt import build_explanation_prompt


def main():

    question = input("Ask a question: ")

    prompt = build_sql_prompt(question)

    sql = generate_response(prompt)

    print("\nGenerated SQL:\n")
    print(sql)

    if not validate_sql(sql):
        print("\nUnsafe SQL detected.")
        return

    columns, results = execute_query(sql)

    print("\nResults:\n")

    if not results:
        print("No records found.")
        return
    
    summary_prompt = build_explanation_prompt(question, results)

    summary = generate_response(summary_prompt)

    print(columns)

    for row in results:
        print(dict(zip(columns, row)))

    print("\nSummary\n")
    print(summary)


if __name__ == "__main__":
    main()