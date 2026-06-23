from tools.resume_tool import ResumeTool

resume_text = """
Anusha Raj

Python
Machine Learning
Deep Learning
PyTorch
TensorFlow
Computer Vision
FastAPI

Built a pneumonia detection system.
Built AI agents using LangGraph.
"""

tool = ResumeTool()

result = tool.execute(
    resume_text=resume_text
)

print(result)