from duckduckgo_search import DDGS


BLOCKED_DOMAINS = [
    ".cn",
    "baidu",
    "zhihu",
    "csdn",
    "weixin",
    "qq.com",
]


def is_valid_url(url: str) -> bool:
    for bad in BLOCKED_DOMAINS:
        if bad in url:
            return False
    return True


def search_web(query: str, max_results: int = 10) -> list[str]:
    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(
            query,
            region="us-en",   # force English
            safesearch="moderate",
            max_results=max_results * 2,
        )

        for r in results:
            url = r.get("href")
            if url and is_valid_url(url):
                urls.append(url)

            if len(urls) >= max_results:
                break

    return urls
