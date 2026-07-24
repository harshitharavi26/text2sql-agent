from rag.embeddings import get_embedding


def main():

    text = "Employee salary information"

    embedding = get_embedding(text)

    print(type(embedding))
    print(len(embedding))

    print("\nFirst 10 values:\n")

    print(embedding[:10])


if __name__ == "__main__":
    main()