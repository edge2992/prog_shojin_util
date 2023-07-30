from urllib.parse import urlparse, urlunparse


def clean_url(url: str) -> str:
    parsed = urlparse(url)
    cleaned = urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
    return cleaned
