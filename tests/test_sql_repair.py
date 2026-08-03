from unittest.mock import patch

from agents.sql_agent import answer_question


def main():
    question = "Show all employees"

    # Force the initial SQL generator to return invalid SQL.
    # The repair agent will still use the real LLM.
    with patch(
        "agents.sql_agent.generate_response",
        return_value="SELECT * FROM employee;",
    ):
        result = answer_question(question)

    print("=" * 70)
    print("Retrieved Schema")
    print("=" * 70)
    print(result["schema"])
    print()

    if result.get("repaired"):
        print("=" * 70)
        print("Original SQL")
        print("=" * 70)
        print(result["original_sql"])
        print()

        print("=" * 70)
        print("Original SQL Error")
        print("=" * 70)
        print(result["original_error"])
        print()

    print("=" * 70)
    print("Final SQL")
    print("=" * 70)
    print(result["sql"])
    print()

    if not result["success"]:
        print("=" * 70)
        print("Repair Failed")
        print("=" * 70)
        print(result["error"])
        return

    print("=" * 70)
    print("Results")
    print("=" * 70)
    print(result["columns"])

    # Print only the first 10 rows.
    for row in result["rows"][:10]:
        print(row)

    print()
    print("=" * 70)
    print("Repair Status")
    print("=" * 70)
    print(f"Success: {result['success']}")
    print(f"Repaired: {result.get('repaired', False)}")


if __name__ == "__main__":
    main()