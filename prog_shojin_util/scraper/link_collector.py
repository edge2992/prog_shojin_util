from typing import Optional

import requests
from bs4 import BeautifulSoup

from prog_shojin_util.utils.url_tools import clean_url


class LinkCollector:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_links(self) -> list[str]:
        content = self._fetch_content()
        if not content:
            return []

        soup = BeautifulSoup(content, "html.parser")
        links = self._extract_links(soup)
        return links

    def _fetch_content(self) -> Optional[str]:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            return None

        return response.text

    def _extract_links(self, soup: BeautifulSoup) -> list[str]:
        link_elements = soup.find_all("a")
        links = [
            link.get("href") for link in link_elements if link.get("href") is not None
        ]
        return links

    def _clean_links(self, links: list[str]) -> list[str]:
        return [clean_url(link) for link in links]

    def fetch_links_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        links = self._extract_links(soup)
        cleaned_links = self._clean_links(links)
        return cleaned_links
