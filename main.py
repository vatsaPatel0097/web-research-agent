import sys
from graph.graph import build_graph


def run(topic: str):
    graph = build_graph()
    return graph.invoke({
        "input": topic,
        "subtopics": [],
        "urls": [],
        "article": "",
        "topic_retry": 0,
        "article_retry": 0,
    })


def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else "Machine Learning in Healthcare"
    result = run(topic)

    print("\n===== SCRAPED SOURCES =====")
    for i, doc in enumerate(result["documents"], start=1):
        print(f"Source {i}: {len(doc.split())} words")

    print("\n===== GENERATED ARTICLE =====\n")
    print(result["article"])


if __name__ == "__main__":
    main()
