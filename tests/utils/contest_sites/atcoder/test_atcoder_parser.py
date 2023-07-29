from prog_shojin_util.utils.contest_sites.abstract import ParsedProblem
from prog_shojin_util.utils.contest_sites.atcoder import AtcoderParser


def test_atcoder_parser():
    # 正しいAtcoderのURL
    valid_url = "https://atcoder.jp/contests/abc121/tasks/abc121_c"

    # パーサーを使用してIDを抽出
    assert AtcoderParser.extract_problem_id(valid_url) == "abc121_c"
    assert AtcoderParser.extract_contest_id(valid_url) == "abc121"
    assert AtcoderParser.parse(valid_url) == ParsedProblem(problem_id="abc121_c")

    # 一致しないURL
    invalid_url = "https://atcoder.jp/contests/abc121"
    assert AtcoderParser.extract_problem_id(invalid_url) is None
    assert AtcoderParser.extract_contest_id(invalid_url) is None
    assert AtcoderParser.parse(invalid_url) is None

    # 一致しないドメインのURL
    another_url = "https://example.com/contests/abc121/tasks/abc121_c"
    assert AtcoderParser.extract_problem_id(another_url) is None
    assert AtcoderParser.extract_contest_id(another_url) is None
    assert AtcoderParser.parse(another_url) is None
