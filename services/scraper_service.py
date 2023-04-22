import logging
import re
import requests, json
from bs4 import BeautifulSoup
from typing import *
import numpy as np


class ContentScraper:
    def __init__(self) -> None:
        pass

    def generate_list_of_pages(
        self, base_url: str, number_of_pages: int, page_param: str = "?page="
    ):
        return [f"{base_url}{page_param}{i}" for i in range(1, number_of_pages + 1)]

    def search_for_pages_in_parent_page(
        self,
        base_url: str,
        path_to_search_for: str,
        root_url: str,
        paths_to_exclude: List[str],
    ) -> List[str]:
        """
        base_url is the url to start scraping from
        path_to_search_for is the URL path that the nested pages must contain
        root_url is the root where the scraped URLs will be appended to
        """
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = []

        for link in soup.find_all("a"):
            href = link.get("href")
            if href.startswith(path_to_search_for) and not any(
                item in href for item in paths_to_exclude
            ):
                links.append(root_url + href)
        return links

    def scrape_all_content_under_tag(self, url: str, article_tag: str, title_tag: str):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            body = soup.find_all(article_tag)[0].text
            title = re.sub(r"[^a-zA-Z0-9\s]", "", soup.find_all(title_tag)[0].text)

            return {"body": body, "title": title}

        except Exception as e:
            logging.warning(f"Could fetch text for title for {url}: {e}")
            return {"body": None, "title": None}
