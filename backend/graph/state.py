from typing import TypedDict


class AgentState(TypedDict):

    user_input: str

    selected_tool: str

    result: dict

    resume_text: str

    job_description: str

    target_role: str