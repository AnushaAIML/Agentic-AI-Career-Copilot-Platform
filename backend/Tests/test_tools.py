from tools.resume_tool import ResumeTool
from tools.jd_match_tool import JDMatchTool
from tools.interview_tool import InterviewTool
from tools.career_advisor_tool import CareerAdvisorTool

tools = [
    ResumeTool(),
    JDMatchTool(),
    InterviewTool(),
    CareerAdvisorTool()
]

for tool in tools:

    metadata = tool.get_metadata()

    print("=" * 50)
    print(metadata.name)
    print(metadata.description)
    print(metadata.input_schema)