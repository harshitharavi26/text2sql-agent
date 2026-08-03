from database.query_executor import execute_query


def main():

    sql = """
    SELECT
        department_name,
        budget
    FROM departments
    LIMIT 5;
    """

    columns, rows = execute_query(sql)

    print(columns)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()