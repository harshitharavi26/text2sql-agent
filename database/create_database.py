import duckdb

DATABASE_PATH = "data/hr_database.duckdb"
SCHEMA_PATH = "database/schema.sql"

# Connect to (or create) the database
#connection = duckdb.connect("data/hr_database.duckdb")

def create_database():
    '''Create a DuckDB database using project schema.'''
    try:
        print("Creating database...")
        with duckdb.connect(DATABASE_PATH) as connection:
            with open(SCHEMA_PATH, 'r') as schema_file:
                schema = schema_file.read()

            connection.execute(schema)

        print("Database schema created successfully.")
    
    except Exception as e:
        print(f"Error creating database: {e}")

def main():
    create_database()

if __name__=="__main__":
    main()
