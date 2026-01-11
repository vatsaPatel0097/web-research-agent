import hashlib


def deduplicate(texts: list[str]) -> list[str]:
    seen = set()
    unique = []

    for text in texts:
        h = hashlib.md5(text.encode("utf-8")).hexdigest()
        if h not in seen:
            seen.add(h)
            unique.append(text)

    return unique


def rank_documents(texts: list[str], min_words: int = 200, max_docs: int = 3) -> list[str]:
    # Basic quality ranking by length
    scored = []

    for text in texts:
        wc = len(text.split())
        if wc >= min_words:
            scored.append((wc, text))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [t for _, t in scored[:max_docs]]


def filter_sources(documents: list[str]) -> list[str]:
    docs = deduplicate(documents)
    docs = rank_documents(docs)
    return docs
