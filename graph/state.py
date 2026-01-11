from typing import TypedDict, List


class GraphState(TypedDict):
    input: str
    subtopics: List[str]
    article: str
