from backend.graph.state import AgentState


def route_query(state: AgentState):

    query = state["user_input"].lower()

    if any(
        keyword in query
        for keyword in [
            "resume",
            "cv",
            "analyze resume",
            "resume analysis"
        ]
    ):
        tool_name = "resume_analyzer"

    elif any(
        keyword in query
        for keyword in [
            "job description",
            "jd",
            "match",
            "compare"
        ]
    ):
        tool_name = "jd_matcher"

    elif any(
        keyword in query
        for keyword in [
            "interview",
            "questions",
            "mock interview"
        ]
    ):
        tool_name = "interview_generator"

    else:
        tool_name = "career_advisor"

    return {
        **state,
        "selected_tool": tool_name
    }