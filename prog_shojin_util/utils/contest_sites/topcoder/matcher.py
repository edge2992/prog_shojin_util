from prog_shojin_util.utils.contest_sites.abstract.matcher import MatcherInterface


class TopcoderMatcher(MatcherInterface):
    _pattern = r"https://.*\.topcoder\.com/.*"
    _key_name = "topcoder"
