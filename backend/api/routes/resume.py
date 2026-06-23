from fastapi import APIRouter

from backend.schemas.api_schema import ResumeRequest
from backend.tools.resume_tool import ResumeTool

router = APIRouter()

tool = ResumeTool()


@router.post("/resume-analysis")
def analyze_resume(request: ResumeRequest):

    return tool.execute(
        resume_text=request.resume_text
    )