from .atcoder import AtcoderMatcher
from .topcoder import TopcoderMatcher
from .yukicoder import YukicoderMatcher


def classify_urls_by_contest_sites(urls: list) -> dict:
    """
    Classify urls by contest sites.
    :param urls: list of urls
    :return: dict of urls classified by contest sites
    """
    contest_sites = [AtcoderMatcher, YukicoderMatcher, TopcoderMatcher]
    classified_urls = {contest_site._key_name: [] for contest_site in contest_sites}
    classified_urls["others"] = []

    for url in urls:
        matched = False
        for contest_site in contest_sites:
            if contest_site.match(url):
                classified_urls[contest_site._key_name].append(url)
                matched = True
                break
        if not matched:
            classified_urls["others"].append(url)

    return classified_urls
