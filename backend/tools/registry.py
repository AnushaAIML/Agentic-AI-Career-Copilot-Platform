from backend.tools.resume_tool import ResumeTool
from backend.tools.jd_matcher import JDMatcherTool
from backend.tools.interview_tool import InterviewTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "resume_analyzer": ResumeTool(),
            "jd_matcher": JDMatcherTool(),
            "interview_generator": InterviewTool()
        }

    def get_tool(self, tool_name):
        return self.tools.get(tool_name)

    def list_tools(self):
        return {
            name: tool.get_metadata()
            for name, tool in self.tools.items()
        }