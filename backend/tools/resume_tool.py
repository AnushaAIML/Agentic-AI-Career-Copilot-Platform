import json
import re

from backend.llm.llm_client import llm
from backend.tools.base_tool import BaseTool
from backend.schemas.tool_schema import ToolMetadata


class ResumeTool(BaseTool):

    def get_metadata(self):

        return ToolMetadata(
            name="resume_analyzer",
            description="Analyze a resume and identify skills",
            input_schema={
                "resume_text": "string"
            }
        )

    def execute(self, **kwargs):

        resume_text = kwargs.get(
            "resume_text",
            ""
        )

        prompt = f"""
You are an expert AI career advisor.

Analyze the resume below.

Return ONLY raw JSON.

Do not use markdown.
Do not wrap the response in code blocks.

Return exactly this schema:

{{
    "summary": "",
    "skills": [],
    "strengths": [],
    "missing_skills": []
}}

Resume:

{resume_text}
"""

        response = llm.invoke(prompt)

        try:

            clean_response = re.sub(
                r"```json|```",
                "",
                response.content
            ).strip()

            return json.loads(clean_response)

        except Exception:

            return {
                "summary": response.content,
                "skills": [],
                "strengths": [],
                "missing_skills": []
            }