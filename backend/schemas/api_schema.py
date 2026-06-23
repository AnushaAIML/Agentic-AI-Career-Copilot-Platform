from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_input: str
    resume_text: str = ""
    job_description: str = ""
    target_role: str = ""


class ResumeRequest(BaseModel):
    resume_text: str


class JDRequest(BaseModel):
    resume_text: str
    job_description: str


class InterviewRequest(BaseModel):
    resume_text: str
    target_role: str


class CareerRequest(BaseModel):
    question: str