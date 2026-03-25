import requests


def detect_site_type(url: str) -> str:
    """
    Basic heuristic:
    - if initial HTML contains useful text, treat as static
    - if page is very thin or script-heavy, treat as dynamic
    """
    try:
        response = requests.get(url, timeout=8, headers={
            "User-Agent": "Mozilla/5.0"
        })
        html = response.text.lower()

        if response.status_code != 200:
            return "dynamic"

        script_count = html.count("<script")
        paragraph_count = html.count("<p")
        div_count = html.count("<div")

        if paragraph_count >= 3:
            return "static"

        if script_count > 15 and paragraph_count < 2 and div_count > 20:
            return "dynamic"

        return "static"
    except Exception:
        return "dynamic"
