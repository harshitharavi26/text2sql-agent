import duckdb

DATABASE_PATH = "data/hr_database.duckdb"


def execute_query(sql_query):
    """
    Execute a SQL query against DuckDB.

    Returns:
        On success:
            columns: List of column names
            rows: Query results

        On failure:
            None
            error message
    """

    try:
        with duckdb.connect(
            DATABASE_PATH,
            read_only=True,
        ) as connection:

            result = connection.execute(sql_query)

            columns = [
                column[0]
                for column in result.description
            ]

            rows = result.fetchall()

            return columns, rows

    except Exception as error:
        return None, str(error)