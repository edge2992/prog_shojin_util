from .abstract_contest import ContestSite


class Atcoder(ContestSite):
    _pattern = r"https://atcoder\.jp.*"
    _key_name = "atcoder"
