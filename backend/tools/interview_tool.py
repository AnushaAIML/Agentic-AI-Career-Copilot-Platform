import json
import re

from backend.llm.llm_client import llm
from backend.tools.base_tool import BaseTool
from backend.schemas.tool_schema import ToolMetadata


class InterviewTool(BaseTool):

    def get_metadata(self):

        return ToolMetadata(
            name="interview_generator",
            description="Generate interview questions based on resume and target role",
            input_schema={
                "resume_text": "string",
                "target_role": "string"
            }
        )

    def execute(self, **kwargs):

        resume_text = kwargs.get(
            "resume_text",
            ""
        )

        target_role = kwargs.get(
            "target_role",
            ""
        )

        prompt = f"""
You are a senior technical interviewer.

Generate:

1. Five technical interview questions
2. Three behavioral interview questions

based on the resume and target role.

Return ONLY valid JSON.

Schema:

{{
    "technical_questions": [
        {{
            "question": "",
            "difficulty": "",
            "expected_answer": ""
        }}
    ],
    "behavioral_questions": [
        {{
            "question": "",
            "difficulty": "",
            "expected_answer": ""
        }}
    ]
}}

Target Role:

{target_role}

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
                "technical_questions": [],
                "behavioral_questions": [],
                "raw_output": response.content
            }