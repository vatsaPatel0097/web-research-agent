from langgraph.graph import StateGraph, END
from graph.state import GraphState
from agents.topic_agent import analyze_topic
from agents.search_agent import search_web
from agents.writer_agent import write_article
from config.settings import (
    MIN_SUBTOPICS,
    MIN_ARTICLE_WORDS,
    MAX_TOPIC_RETRY,
    MAX_ARTICLE_RETRY,
)


def topic_node(state: GraphState) -> GraphState:
    return {"subtopics": analyze_topic(state["input"])}


def validate_subtopics(state: GraphState):
    if len(state["subtopics"]) < MIN_SUBTOPICS and state["topic_retry"] < MAX_TOPIC_RETRY:
        return "retry_topic"
    return "search"


def retry_topic_node(state: GraphState) -> GraphState:
    return {"topic_retry": state["topic_retry"] + 1}


def search_node(state: GraphState) -> GraphState:
    urls = search_web(state["input"])
    return {"urls": urls}


def writer_node(state: GraphState) -> GraphState:
    return {"article": write_article(state["input"], state["subtopics"])}


def validate_article(state: GraphState):
    if len(state["article"].split()) < MIN_ARTICLE_WORDS and state["article_retry"] < MAX_ARTICLE_RETRY:
        return "retry_article"
    return "end"


def retry_article_node(state: GraphState) -> GraphState:
    return {"article_retry": state["article_retry"] + 1}


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("topic_node", topic_node)
    graph.add_node("retry_topic_node", retry_topic_node)
    graph.add_node("search_node", search_node)
    graph.add_node("writer_node", writer_node)
    graph.add_node("retry_article_node", retry_article_node)

    graph.set_entry_point("topic_node")

    graph.add_conditional_edges(
        "topic_node",
        validate_subtopics,
        {"retry_topic": "retry_topic_node", "search": "search_node"},
    )

    graph.add_edge("retry_topic_node", "topic_node")
    graph.add_edge("search_node", "writer_node")

    graph.add_conditional_edges(
        "writer_node",
        validate_article,
        {"retry_article": "retry_article_node", "end": END},
    )

    graph.add_edge("retry_article_node", "writer_node")

    return graph.compile()
