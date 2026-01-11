from langgraph.graph import StateGraph, END
from graph.state import GraphState
from agents.topic_agent import analyze_topic
from agents.writer_agent import write_article


def topic_node(state: GraphState) -> GraphState:
    topic = state["input"]
    subtopics = analyze_topic(topic)
    return {"subtopics": subtopics}


def writer_node(state: GraphState) -> GraphState:
    article = write_article(state["input"], state["subtopics"])
    return {"article": article}


def output_node(state: GraphState) -> GraphState:
    return state


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("topic_node", topic_node)
    graph.add_node("writer_node", writer_node)
    graph.add_node("output_node", output_node)

    graph.set_entry_point("topic_node")
    graph.add_edge("topic_node", "writer_node")
    graph.add_edge("writer_node", "output_node")
    graph.add_edge("output_node", END)

    return graph.compile()
