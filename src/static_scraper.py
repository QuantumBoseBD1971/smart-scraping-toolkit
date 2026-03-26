import requests
from bs4 import BeautifulSoup


def scrape_static(url: str):
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

    paragraphs = [
        p.get_text(" ", strip=True)
        for p in soup.find_all("p")
        if p.get_text(strip=True)
    ]

    headings = []
    for tag in ["h1", "h2", "h3"]:
        headings.extend(
            h.get_text(" ", strip=True)
            for h in soup.find_all(tag)
            if h.get_text(strip=True)
        )

    links = []
    for a in soup.find_all("a", href=True):
        text = a.get_text(" ", strip=True)
        href = a["href"]
        if href:
            links.append({
                "text": text,
                "href": href
            })

    return {
        "url": url,
        "scrape_mode": "static",
        "title": title,
        "headings": headings[:20],
        "paragraphs": paragraphs[:20],
        "links": links[:50]
    }
