import json
from utils.llm import generate


def analyze_topic(topic: str) -> list[str]:
    prompt = f"""
You are a research assistant.
Given a topic, generate 5 clear, non-overlapping subtopics.
Return ONLY a JSON array of strings.

Topic: {topic}
"""

    response = generate(prompt, model="phi")

    try:
        subtopics = json.loads(response)
        if isinstance(subtopics, list):
            return subtopics
    except Exception:
        pass

    return []
