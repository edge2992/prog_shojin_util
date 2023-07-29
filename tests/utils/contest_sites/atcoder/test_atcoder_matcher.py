from prog_shojin_util.utils.contest_sites.atcoder import AtcoderMatcher


def test_atcoder_matcher():
    matcher = AtcoderMatcher()

    # 正しいAtcoderのURL
    valid_url = "https://atcoder.jp/contests/abc121/tasks/abc121_c"
    assert matcher.match(valid_url)

    # 一致しないURL
    invalid_url = "https://atcoder.jp/contests/abc121"
    assert not matcher.match(invalid_url)

    # 一致しないドメインのURL
    another_url = "https://example.com/contests/abc121/tasks/abc121_c"
    assert not matcher.match(another_url)
