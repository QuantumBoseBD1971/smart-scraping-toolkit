from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def scrape_dynamic(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=30000)

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")

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
        "scrape_mode": "dynamic",
        "title": title,
        "headings": headings[:20],
        "paragraphs": paragraphs[:20],
        "links": links[:50]
    }
