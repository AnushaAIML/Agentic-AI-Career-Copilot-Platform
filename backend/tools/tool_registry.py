from backend.tools.resume_tool import ResumeTool
from backend.tools.jd_match_tool import JDMatchTool
from backend.tools.interview_tool import InterviewTool

TOOLS = {
    "resume_analyzer": ResumeTool(),
    "jd_matcher": JDMatchTool(),
    "interview_generator": InterviewTool(),
}