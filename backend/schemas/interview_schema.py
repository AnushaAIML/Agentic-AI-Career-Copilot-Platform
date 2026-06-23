from pydantic import BaseModel
from typing import List


class InterviewQuestion(BaseModel):
    question: str
    difficulty: str
    expected_answer: str


class InterviewResult(BaseModel):
    technical_questions: List[InterviewQuestion]
    behavioral_questions: List[InterviewQuestion]