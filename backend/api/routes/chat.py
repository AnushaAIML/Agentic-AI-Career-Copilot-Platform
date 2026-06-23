from fastapi import APIRouter

from backend.schemas.api_schema import ChatRequest
from backend.graph.workflow import build_graph

router = APIRouter()

agent = build_graph()


@router.post("/chat")
def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "user_input": request.user_input,
            "resume_text": request.resume_text,
            "job_description": request.job_description,
            "target_role": request.target_role
        }
    )

    return result