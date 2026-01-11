from utils.llm import generate


def write_article(topic: str, subtopics: list[str]) -> str:
    joined = "\n".join([f"- {s}" for s in subtopics])

    prompt = f"""
You are an article writer.

Write a clear, informative article on the topic below.
Use the provided subtopics as section headings.
Minimum length: 500 words.
No markdown. Plain text only.

Topic: {topic}

Subtopics:
{joined}
"""

    return generate(prompt, model="phi")
