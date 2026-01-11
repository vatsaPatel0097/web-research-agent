import sys
from graph.graph import build_graph

def main():
    graph = build_graph()

    topic = sys.argv[1] if len(sys.argv) > 1 else "Test Topic"

    result = graph.invoke({"input": topic})
    print(result["output"])

if __name__ == "__main__":
    main()
