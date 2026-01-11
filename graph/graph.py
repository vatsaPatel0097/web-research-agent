from langgraph.graph import StateGraph, END
from graph.state import GraphState


def input_node(state: GraphState) -> GraphState:
    return {"input": state["input"]}


def output_node(state: GraphState) -> GraphState:
    text = state["input"]
    return {"output": f"Processed input: {text}"}


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("input_node", input_node)
    graph.add_node("output_node", output_node)

    graph.set_entry_point("input_node")
    graph.add_edge("input_node", "output_node")
    graph.add_edge("output_node", END)

    return graph.compile()
