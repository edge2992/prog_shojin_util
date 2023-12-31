from prog_shojin_util.utils.contest_sites import classify_urls_by_contest_sites


def test_classify_urls_by_contest_sites():
    # 入力として与えるURLのリスト
    urls = [
        "https://atcoder.jp/contests/abc123/tasks/abc123_a",
        "https://yukicoder.me/problems/no/1234",
        "https://www.topcoder.com/challenges/12345",
        "https://unknownsite.com/contest/xyz",
    ]

    # 期待される出力
    expected_output = {
        "atcoder": ["https://atcoder.jp/contests/abc123/tasks/abc123_a"],
        "yukicoder": ["https://yukicoder.me/problems/no/1234"],
        "topcoder": ["https://www.topcoder.com/challenges/12345"],
        "others": ["https://unknownsite.com/contest/xyz"],
    }

    result = classify_urls_by_contest_sites(urls)

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
