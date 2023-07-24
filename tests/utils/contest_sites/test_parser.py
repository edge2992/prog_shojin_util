from atcoder_util_problem.utils.contest_sites.atcoder import AtcoderParser


def test_atcoder_parser():
    # 正しいAtcoderのURL
    valid_url = "https://atcoder.jp/contests/abc121/tasks/abc121_c"

    # パーサーを使用してIDを抽出
    assert AtcoderParser.extract_problem_id(valid_url) == "abc121_c"
    assert AtcoderParser.extract_contest_id(valid_url) == "abc121"
    assert AtcoderParser.get_contest_and_problem_id(valid_url) == {
        "problem_id": "abc121_c",
        "contest_id": "abc121",
    }

    # 一致しないURL
    invalid_url = "https://atcoder.jp/contests/abc121"
    assert AtcoderParser.extract_problem_id(invalid_url) is None
    assert AtcoderParser.extract_contest_id(invalid_url) is None
    assert AtcoderParser.get_contest_and_problem_id(invalid_url) == {
        "problem_id": None,
        "contest_id": None,
    }

    # 一致しないドメインのURL
    another_url = "https://example.com/contests/abc121/tasks/abc121_c"
    assert AtcoderParser.extract_problem_id(another_url) is None
    assert AtcoderParser.extract_contest_id(another_url) is None
    assert AtcoderParser.get_contest_and_problem_id(another_url) == {
        "problem_id": None,
        "contest_id": None,
    }
