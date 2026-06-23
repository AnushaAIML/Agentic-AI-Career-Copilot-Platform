import json
import re

from backend.llm.llm_client import llm
from backend.tools.base_tool import BaseTool
from backend.schemas.tool_schema import ToolMetadata


class JDMatchTool(BaseTool):

    def get_metadata(self):

        return ToolMetadata(
            name="jd_matcher",
            description="Compare resume against job description",
            input_schema={
                "resume_text": "string",
                "job_description": "string"
            }
        )

    def execute(self, **kwargs):

        resume_text = kwargs.get(
            "resume_text",
            ""
        )

        job_description = kwargs.get(
            "job_description",
            ""
        )

        prompt = f"""
You are an expert AI recruiter.

Compare the candidate resume against the job description.

Return ONLY valid JSON.

Schema:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "recommendations": []
}}

Resume:

{resume_text}

Job Description:

{job_description}
"""

        response = llm.invoke(prompt)

        try:

            clean_response = re.sub(
                r"```json|```",
                "",
                response.content
            ).strip()

            return json.loads(
                clean_response
            )

        except Exception:

            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
                "recommendations": [
                    response.content
                ]
            }