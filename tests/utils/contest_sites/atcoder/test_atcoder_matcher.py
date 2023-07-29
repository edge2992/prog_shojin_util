from prog_shojin_util.utils.contest_sites.atcoder import AtcoderMatcher


def test_atcoder_matcher():
    matcher = AtcoderMatcher()

    # 正しいAtcoderのURL
    valid_url = "https://atcoder.jp/contests/abc121/tasks/abc121_c"
    assert matcher.match(valid_url) == True

    # 一致しないURL
    invalid_url = "https://atcoder.jp/contests/abc121"
    assert matcher.match(invalid_url) == False

    # 一致しないドメインのURL
    another_url = "https://example.com/contests/abc121/tasks/abc121_c"
    assert matcher.match(another_url) == False
