def extract_summary(scraped_payload: dict) -> dict:
    return {
        "title": scraped_payload.get("title"),
        "paragraph_count": len(scraped_payload.get("paragraphs", [])),
        "link_count": len(scraped_payload.get("links", [])),
        "scrape_mode": scraped_payload.get("scrape_mode"),
    }
