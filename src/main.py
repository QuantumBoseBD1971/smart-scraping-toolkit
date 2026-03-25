import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from detector import detect_site_type
from static_scraper import scrape_static
from dynamic_scraper import scrape_dynamic


def parse_args():
    parser = argparse.ArgumentParser(
        description="Smart Scraping Toolkit - scrape structured data from static or dynamic websites."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Target URL to scrape"
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Directory to save JSON output (default: output)"
    )
    return parser.parse_args()


def safe_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.replace(".", "_") or "site"
    path = parsed.path.strip("/").replace("/", "_")

    if path:
        return f"{host}__{path}.json"
    return f"{host}.json"


def save_output(payload: dict, url: str, output_dir: str):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / safe_name_from_url(url)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    return output_file


def run(url: str, output_dir: str):
    print(f"\nProcessing: {url}")

    site_type = detect_site_type(url)
    print(f"Detected site type: {site_type}")

    if site_type == "static":
        data = scrape_static(url)
    else:
        data = scrape_dynamic(url)

    output_path = save_output(data, url, output_dir)

    print("\nScrape complete")
    print(f"Title: {data.get('title')}")
    print(f"Paragraph count: {len(data.get('paragraphs', []))}")
    print(f"Link count: {len(data.get('links', []))}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    args = parse_args()
    run(args.url, args.output)
