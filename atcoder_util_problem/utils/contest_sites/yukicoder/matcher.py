from ..abstract_contest import ContestSiteMatcher


class YukicoderMatcher(ContestSiteMatcher):
    _pattern = r"https://yukicoder\.me/.*"
    _key_name = "yukicoder"
