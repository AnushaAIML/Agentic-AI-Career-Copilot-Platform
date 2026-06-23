from langgraph.graph import StateGraph

from backend.graph.state import AgentState
from backend.graph.router import route_query
from backend.graph.nodes import execute_tool


def build_graph():

    workflow = StateGraph(
        AgentState
    )

    workflow.add_node(
        "router",
        route_query
    )

    workflow.add_node(
        "executor",
        execute_tool
    )

    workflow.set_entry_point(
        "router"
    )

    workflow.add_edge(
        "router",
        "executor"
    )

    return workflow.compile()