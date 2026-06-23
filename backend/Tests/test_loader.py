from backend.rag.loader import load_documents

docs = load_documents("backend/knowledge_base")

print(f"\nLoaded {len(docs)} documents\n")

for doc in docs:
    print(doc["source"])