from llm.llm_client import llm

response = llm.invoke(
    "Explain machine learning in one sentence."
)

print(response.content)