from typing import TypedDict, List


class GraphState(TypedDict):
    input: str
    subtopics: List[str]
    urls: List[str]
    documents: List[str]
    article: str
    topic_retry: int
    article_retry: int
