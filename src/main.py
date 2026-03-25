from detector import is_static_site
from static_scraper import scrape_static
# dynamic_scraper will come later


def run(url):
    print(f"Processing: {url}")

    if is_static_site(url):
        print("Detected: STATIC site")
        data = scrape_static(url)
    else:
        print("Detected: DYNAMIC site (fallback to static for now)")
        data = scrape_static(url)

    print(data)


if __name__ == "__main__":
    test_url = "https://example.com"
    run(test_url)
