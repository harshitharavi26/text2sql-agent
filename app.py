from agents.sql_agent import answer_question


def main():

    question = input("Ask a question: ")

    result = answer_question(question)

    print("\nGenerated SQL:\n")
    print(result["sql"])

    if not result["success"]:
        print("\nError:\n")
        print(result["error"])
        return

    if result["repaired"]:
        print("\nThe original SQL failed and was repaired.")

        print("\nOriginal SQL:\n")
        print(result["original_sql"])

        print("\nOriginal Error:\n")
        print(result["original_error"])

    print("\nResults:\n")
    print(result["columns"])

    for row in result["rows"]:
        print(dict(zip(result["columns"], row)))


if __name__ == "__main__":
    main()