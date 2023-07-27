from ..abstract import MatcherInterface


class AtcoderMatcher(MatcherInterface):
    _pattern = r"https://atcoder\.jp.*"
    _key_name = "atcoder"
