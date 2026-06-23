from tools.interview_tool import InterviewTool

resume_text = """
Python
Machine Learning
Deep Learning
PyTorch
TensorFlow
Computer Vision
FastAPI
LangGraph

Built a pneumonia detection system.
Built AI agents using LangGraph.
"""

target_role = "AI Engineer"

tool = InterviewTool()

result = tool.execute(
    resume_text=resume_text,
    target_role=target_role
)

print(result)