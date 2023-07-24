from .abstract_contest import ContestSite


class Topcoder(ContestSite):
    _pattern = r"https://.*\.topcoder\.com/.*"
    _key_name = "topcoder"
