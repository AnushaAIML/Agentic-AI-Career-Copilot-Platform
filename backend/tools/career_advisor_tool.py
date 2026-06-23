from backend.llm.llm_client import llm
from backend.rag.retriever import retrieve

from backend.tools.base_tool import BaseTool
from backend.schemas.tool_schema import ToolMetadata


class CareerAdvisorTool(BaseTool):

    def get_metadata(self):
        return ToolMetadata(
            name="career_advisor",
            description="Answer career questions using RAG",
            input_schema={
                "question": "string"
            }
        )

    # ✅ FIX: must be execute (NOT run)
    def execute(self, input_data: dict):
        question = input_data.get("question", "")

        # retrieve context
        context = retrieve(question)

        # LLM call
        response = llm.invoke(f"""
You are a career advisor AI.

Context:
{context}

Question:
{question}

Give a helpful answer.
""")

        return {
            "answer": response
        }