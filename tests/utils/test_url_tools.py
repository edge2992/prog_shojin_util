import pytest

from prog_shojin_util.utils.url_tools import clean_url


@pytest.mark.parametrize(
    "input_url,expected_output",
    [
        (
            "https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja",
            "https://atcoder.jp/contests/abc075/tasks/abc075_c",
        ),
        (
            "https://yukicoder.me/problems/no/2?user=123",
            "https://yukicoder.me/problems/no/2",
        ),
        (
            "https://example.com/page/path?query=value&another=thing",
            "https://example.com/page/path",
        ),
        ("https://example.com/no/query/params", "https://example.com/no/query/params"),
    ],
)
def test_clean_url(input_url, expected_output):
    assert clean_url(input_url) == expected_output
