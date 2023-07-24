from ..abstract_contest import ContestSiteMatcher


class TopcoderMatcher(ContestSiteMatcher):
    _pattern = r"https://.*\.topcoder\.com/.*"
    _key_name = "topcoder"
