from backend.tools.tool_registry import TOOLS


def execute_tool(state):

    tool_name = state["selected_tool"]

    tool = TOOLS[tool_name]

    if tool_name == "career_advisor":

        result = tool.execute(
            question=state["user_input"]
        )

    elif tool_name == "resume_analyzer":

        result = tool.execute(
            resume_text=state.get(
                "resume_text",
                ""
            )
        )

    elif tool_name == "jd_matcher":

        result = tool.execute(
            resume_text=state.get(
                "resume_text",
                ""
            ),
            job_description=state.get(
                "job_description",
                ""
            )
        )

    elif tool_name == "interview_generator":

        result = tool.execute(
            resume_text=state.get(
                "resume_text",
                ""
            ),
            target_role=state.get(
                "target_role",
                "AI Engineer"
            )
        )

    else:

        result = {
            "error": "unknown tool"
        }

    return {
        **state,
        "result": result
    }