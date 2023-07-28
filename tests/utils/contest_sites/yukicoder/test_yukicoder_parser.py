from prog_shojin_util.utils.contest_sites.yukicoder import YukicoderParser


def test_yukicoder_parser():
    # 正しいyukicoderのURL
    valid_url = "https://yukicoder.me/problems/no/2391"

    # パーサーを使用してIDを抽出
    assert YukicoderParser.extract_problem_id(valid_url) == "2391"
    assert YukicoderParser.parse(valid_url) == {
        "No": "2391",
    }

    # 一致しないURL
    invalid_url = "https://yukicoder.me/problems/no/"
    assert YukicoderParser.extract_problem_id(invalid_url) is None
    assert YukicoderParser.parse(invalid_url) == {
        "No": None,
    }

    # 一致しないドメインのURL
    another_url = "https://example.com/problems/no/2391"
    assert YukicoderParser.extract_problem_id(another_url) is None
    assert YukicoderParser.parse(another_url) == {
        "No": None,
    }

    # URLパターンが異なる場合
    another_pattern = "https://yukicoder.me/problems/2391"
    assert YukicoderParser.extract_problem_id(another_pattern) is None
    assert YukicoderParser.parse(another_pattern) == {
        "No": None,
    }
