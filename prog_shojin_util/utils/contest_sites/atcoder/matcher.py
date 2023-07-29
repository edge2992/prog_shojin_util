from ..abstract import MatcherInterface


class AtcoderMatcher(MatcherInterface):
    _pattern = r"https://atcoder\.jp/contests/(?P<contest_id>[^/]+)/tasks/(?P<problem_id>[^/]+)"  # noqa: E501
    _key_name = "atcoder"
