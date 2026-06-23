from fastapi import APIRouter
from backend.llm.llm_client import llm
from backend.rag.retriever import retrieve

router = APIRouter()

@router.post("/career-advice")
def career_advice(payload: dict):
    try:
        question = payload.get("question", "")

        if not question:
            return {"error": "Question is empty"}

        context = retrieve(question)

        response = llm.invoke(f"""
You are a career advisor AI.

Context:
{context}

Question:
{question}

Give a clear answer.
""")

        return {
            "answer": response,
            "sources": ["rag", "llm"]
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}