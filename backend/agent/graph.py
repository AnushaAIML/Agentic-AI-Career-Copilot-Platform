from langgraph.graph import StateGraph
from langgraph.graph import END

from backend.agent.state import AgentState
from backend.agent.nodes import (
    planner_node,
    tool_node,
    response_node
)


builder = StateGraph(AgentState)

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "tool_executor",
    tool_node
)

builder.add_node(
    "response",
    response_node
)

builder.set_entry_point(
    "planner"
)

builder.add_edge(
    "planner",
    "tool_executor"
)

builder.add_edge(
    "tool_executor",
    "response"
)

builder.add_edge(
    "response",
    END
)

graph = builder.compile()