import pytest
from bs4 import BeautifulSoup
from atcoder_util_problem.scraper.link_collector import LinkCollector


@pytest.fixture
def collector():
    return LinkCollector("https://example.com")


@pytest.fixture
def test_html_content():
    return """
    <html>
        <body>
            <a href="https://example.com/problem1">Problem 1</a>
            <a href="https://example.com/problem2">Problem 2</a>
            <a href="https://example.com/problem3">Problem 3</a>
        </body>
    </html>
    """


def test_extract_links(collector, test_html_content):
    soup = BeautifulSoup(test_html_content, "html.parser")
    links = collector._extract_links(soup)
    expected_links = [
        "https://example.com/problem1",
        "https://example.com/problem2",
        "https://example.com/problem3",
    ]
    assert links == expected_links


def test_fetch_links_from_file(collector, test_html_content, tmp_path):
    # tmp_path is a pytest fixture for temporary directory
    test_file = tmp_path / "test_file.html"
    test_file.write_text(test_html_content)

    links = collector.fetch_links_from_file(str(test_file))
    expected_links = [
        "https://example.com/problem1",
        "https://example.com/problem2",
        "https://example.com/problem3",
    ]
    assert links == expected_links
