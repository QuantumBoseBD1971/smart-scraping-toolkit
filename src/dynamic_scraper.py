# placeholder for future Playwright-based scraping
from static_scraper import scrape_static


def scrape_dynamic(url: str):
    """
    Temporary fallback until Playwright is added.
    Keeps pipeline working while preserving architecture.
    """
    data = scrape_static(url)
    data["scrape_mode"] = "dynamic-fallback"
    data["note"] = "Dynamic scraper not implemented yet. Used static fallback."
    return data
