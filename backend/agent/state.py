from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    selected_tool: str
    tool_output: dict
    final_response: str