from rag.embeddings import get_embedding
from rag.similarity import cosine_similarity

documents = [
    "Employee salary information",
    "Department budget report",
    "Machine learning models",
    "Pizza recipes",
    "Employee payroll details"
]

query = "Employee compensation"

query_embedding = get_embedding(query)

document_embeddings = [
    get_embedding(doc)
    for doc in documents
]

for doc, embedding in zip(documents, document_embeddings):

    score = cosine_similarity(
        query_embedding,
        embedding
    )

    print(f"{score:.4f} -> {doc}")

