import requests
from bs4 import BeautifulSoup


def scrape_static(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title"

    paragraphs = [p.get_text() for p in soup.find_all("p")]

    return {
        "url": url,
        "title": title,
        "paragraphs": paragraphs[:5]
    }
