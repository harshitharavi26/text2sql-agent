from rag.vector_store import load_schema, search_schema

def main():

    load_schema()

    results = search_schema(
        "Show average salary by department"
    )

    print(results)

if __name__ == "__main__":
    main()