from ..abstract_contest import ContestSiteMatcher


class AtcoderMatcher(ContestSiteMatcher):
    _pattern = r"https://atcoder\.jp.*"
    _key_name = "atcoder"
