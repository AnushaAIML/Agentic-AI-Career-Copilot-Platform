from fastapi import APIRouter

from backend.schemas.api_schema import InterviewRequest
from backend.tools.interview_tool import InterviewTool

router = APIRouter()

tool = InterviewTool()


@router.post("/interview")
def generate_interview(request: InterviewRequest):

    result = tool.execute(
        resume_text=request.resume_text,
        target_role=request.target_role
    )

    return result