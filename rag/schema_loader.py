import duckdb

DATABASE_PATH = "data/hr_database.duckdb"


def get_tables():
    """Return all table names in the database."""

    with duckdb.connect(DATABASE_PATH) as connection:
        tables = connection.execute("SHOW TABLES").fetchall()

    return [table[0] for table in tables]


def get_table_schema(table_name):
    """Return schema information for a table."""

    with duckdb.connect(DATABASE_PATH) as connection:
        schema = connection.execute(
            f"DESCRIBE {table_name}"
        ).fetchall()

    return schema


def generate_schema_documents():
    """
    Generate schema documents from the database.

    Returns:
        List of dictionaries compatible with ChromaDB.
    """

    documents = []

    tables = get_tables()

    for table in tables:

        schema = get_table_schema(table)

        document = f"Table: {table}\n\nColumns:\n"

        for column_name, data_type, *_ in schema:
            document += f"{column_name} ({data_type})\n"

        documents.append(
            {
                "id": table,
                "document": document,
                "metadata": {
                    "table": table
                },
            }
        )

    return documents


if __name__ == "__main__":

    schema_documents = generate_schema_documents()

    for document in schema_documents:
        print("=" * 60)
        print(document["document"])