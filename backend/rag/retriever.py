from backend.rag.loader import load_documents
from backend.rag.vector_store import FAISSStore


store = FAISSStore()

docs = load_documents(
    "backend/knowledge_base"
)

store.build(docs)


def retrieve(query):

    return store.search(query)