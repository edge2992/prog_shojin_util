from .abstract_contest import ContestSite


class Yukicoder(ContestSite):
    _pattern = r"https://yukicoder\.me/.*"
    _key_name = "yukicoder"
