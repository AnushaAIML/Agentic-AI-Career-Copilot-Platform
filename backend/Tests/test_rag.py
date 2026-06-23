from backend.rag.retriever import retrieve
import pprint

results = retrieve(
    "What should I learn for a Generative AI Engineer role?"
)

print("\nRESULTS:\n")
pprint.pprint(results)