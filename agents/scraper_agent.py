import requests
from bs4 import BeautifulSoup


def scrape_url(url: str, timeout: int = 10) -> str:
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=timeout,
        )
        response.raise_for_status()
    except Exception:
        return ""

    soup = BeautifulSoup(response.text, "lxml")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # Clean whitespace
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned_text = " ".join(lines)

    return cleaned_text
