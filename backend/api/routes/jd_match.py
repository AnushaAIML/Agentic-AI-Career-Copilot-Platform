from fastapi import APIRouter

from backend.schemas.api_schema import JDRequest
from backend.tools.jd_match_tool import JDMatchTool

router = APIRouter()

tool = JDMatchTool()


@router.post("/jd-match")
def jd_match(request: JDRequest):

    return tool.execute(
        resume_text=request.resume_text,
        job_description=request.job_description
    )