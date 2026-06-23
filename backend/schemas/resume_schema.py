from pydantic import BaseModel
from typing import List


class ResumeAnalysis(BaseModel):
    summary: str
    skills: List[str]
    strengths: List[str]
    missing_skills: List[str]