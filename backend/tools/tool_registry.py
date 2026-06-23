from backend.tools.resume_tool import ResumeTool
from backend.tools.jd_match_tool import JDMatchTool
from backend.tools.interview_tool import InterviewTool
from backend.tools.career_advisor_tool import CareerAdvisorTool


TOOLS = {
    "resume_analyzer": ResumeTool(),
    "jd_matcher": JDMatchTool(),
    "interview_generator": InterviewTool(),
    "career_advisor": CareerAdvisorTool(),
}