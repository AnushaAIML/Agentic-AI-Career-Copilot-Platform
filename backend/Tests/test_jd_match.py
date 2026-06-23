from tools.jd_match_tool import JDMatchTool

resume_text = """
Python
Machine Learning
Deep Learning
PyTorch
TensorFlow
Computer Vision
FastAPI
LangGraph
"""

job_description = """
We are hiring an AI Engineer.

Requirements:

Python
Machine Learning
Deep Learning
Docker
AWS
FastAPI
LLMs
RAG
Vector Databases
"""

tool = JDMatchTool()

result = tool.execute(
    resume_text=resume_text,
    job_description=job_description
)

print(result)