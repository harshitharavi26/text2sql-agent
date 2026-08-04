from agents.sql_agent_old import answer_question


def main():

    question = "Show average salary by department"

    schema, sql, columns, rows = answer_question(question)

    print("=" * 70)
    print("Retrieved Schema")
    print("=" * 70)
    print(schema)

    print()

    print("=" * 70)
    print("Generated SQL")
    print("=" * 70)
    print(sql)

    print()

    print("=" * 70)
    print("Results")
    print("=" * 70)

    print(columns)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()