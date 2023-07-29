from prog_shojin_util.utils.contest_sites.abstract.matcher import MatcherInterface


class YukicoderMatcher(MatcherInterface):
    _pattern = r"https://yukicoder\.me/problems/no/(\d+)"
    _key_name = "yukicoder"
