import chromadb

from rag import schema_documents
from rag import embeddings
from rag.embeddings import get_embedding
#from rag.schema_documents import SCHEMA_DOCUMENTS
from rag.schema_loader import generate_schema_documents

client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(
    name="schema_collection"
)

def load_schema():

    #embeddings = []
    if collection.count() > 0:
        collection.delete(ids=collection.get()["ids"])

    schema_documents = generate_schema_documents()

    # for doc in schema_documents:
    #     embedding = get_embedding(doc["document"])
    #     embeddings.append(embedding)

    # collection.add(
    #     ids=[doc["id"] for doc in schema_documents],
    #     documents=[doc["document"] for doc in schema_documents],
    #     metadatas=[doc["metadata"] for doc in schema_documents],
    #     embeddings=embeddings,
    # )

    embeddings = [
    get_embedding(doc["document"])
    for doc in schema_documents
]

    collection.add(
        ids=[doc["id"] for doc in schema_documents],
        documents=[doc["document"] for doc in schema_documents],
        metadatas=[doc["metadata"] for doc in schema_documents],
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

def get_schema_context(query, top_k=3):

    results = search_schema(query, top_k)

    documents = results["documents"][0]

    return "\n\n".join(documents)

if __name__ == "__main__":
    load_schema()