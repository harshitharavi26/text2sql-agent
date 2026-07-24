import duckdb

DATABASE_PATH = "data/hr_database.duckdb"


def execute_query(sql: str):
    """
    Execute SQL query and return results.
    """

    try:
        with duckdb.connect(DATABASE_PATH) as connection:

            results = connection.execute(sql).fetchall()

            columns = [
                column[0]
                for column in connection.description
            ]

            return columns, results

    except Exception as e:
        print(f"Database Error: {e}")

        return [], []