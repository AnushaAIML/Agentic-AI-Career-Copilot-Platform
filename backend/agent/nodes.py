from backend.tools.registry import ToolRegistry


registry = ToolRegistry()


def planner_node(state):

    query = state["user_query"].lower()

    if "resume" in query:
        tool = "resume_analyzer"

    elif "job" in query:
        tool = "jd_matcher"

    elif "interview" in query:
        tool = "interview_generator"

    else:
        tool = None

    state["selected_tool"] = tool

    return state


def tool_node(state):

    tool_name = state["selected_tool"]

    if tool_name is None:

        state["tool_output"] = {
            "message": "No tool selected"
        }

        return state

    tool = registry.get_tool(tool_name)

    result = tool.execute()

    state["tool_output"] = result

    return state


def response_node(state):

    state["final_response"] = str(
        state["tool_output"]
    )

    return state