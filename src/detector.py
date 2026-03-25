import requests


def is_static_site(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200 and "<html" in response.text.lower()
    except Exception:
        return False
