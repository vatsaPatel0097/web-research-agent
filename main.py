import sys
from graph.graph import build_graph


def main():
    graph = build_graph()

    topic = sys.argv[1] if len(sys.argv) > 1 else "Artificial Intelligence"

    result = graph.invoke({
        "input": topic,
        "subtopics": [],
        "article": "",
        "topic_retry": 0,
        "article_retry": 0,
    })

    print("\n===== GENERATED ARTICLE =====\n")
    print(result["article"])


if __name__ == "__main__":
    main()
