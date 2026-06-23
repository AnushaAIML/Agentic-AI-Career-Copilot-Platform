from tools.career_advisor_tool import CareerAdvisorTool

tool = CareerAdvisorTool()

result = tool.execute(
    question="What should I learn to become a Generative AI Engineer?"
)

print(result)