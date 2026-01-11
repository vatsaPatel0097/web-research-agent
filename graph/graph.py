from langgraph.graph import StateGraph, END
from graph.state import GraphState
from agents.topic_agent import analyze_topic
from agents.writer_agent import write_article


MAX_TOPIC_RETRY = 2
MAX_ARTICLE_RETRY = 2


def topic_node(state: GraphState) -> GraphState:
    subtopics = analyze_topic(state["input"])
    return {"subtopics": subtopics}


def validate_subtopics(state: GraphState):
    if len(state["subtopics"]) < 3 and state["topic_retry"] < MAX_TOPIC_RETRY:
        return "retry_topic"
    return "write"


def retry_topic_node(state: GraphState) -> GraphState:
    return {"topic_retry": state["topic_retry"] + 1}


def writer_node(state: GraphState) -> GraphState:
    article = write_article(state["input"], state["subtopics"])
    return {"article": article}


def validate_article(state: GraphState):
    word_count = len(state["article"].split())
    if word_count < 300 and state["article_retry"] < MAX_ARTICLE_RETRY:
        return "retry_article"
    return "end"


def retry_article_node(state: GraphState) -> GraphState:
    return {"article_retry": state["article_retry"] + 1}


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("topic_node", topic_node)
    graph.add_node("retry_topic_node", retry_topic_node)
    graph.add_node("writer_node", writer_node)
    graph.add_node("retry_article_node", retry_article_node)

    graph.set_entry_point("topic_node")

    graph.add_conditional_edges(
        "topic_node",
        validate_subtopics,
        {
            "retry_topic": "retry_topic_node",
            "write": "writer_node",
        },
    )

    graph.add_edge("retry_topic_node", "topic_node")

    graph.add_conditional_edges(
        "writer_node",
        validate_article,
        {
            "retry_article": "retry_article_node",
            "end": END,
        },
    )

    graph.add_edge("retry_article_node", "writer_node")

    return graph.compile()
