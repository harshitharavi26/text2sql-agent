import chromadb

from rag.embeddings import get_embedding
from rag.schema_documents import SCHEMA_DOCUMENTS

client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(
    name="schema_collection"
)

def load_schema():

    embeddings = []

    for doc in SCHEMA_DOCUMENTS:
        embedding = get_embedding(doc["document"])
        embeddings.append(embedding)

    collection.add(
        ids=[doc["id"] for doc in SCHEMA_DOCUMENTS],
        documents=[doc["document"] for doc in SCHEMA_DOCUMENTS],
        metadatas=[doc["metadata"] for doc in SCHEMA_DOCUMENTS],
        embeddings=embeddings,
    )

    print("Schema loaded successfully.")

def search_schema(query, top_k=3):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results


if __name__ == "__main__":
    load_schema()