from .contest_sites.atcoder import AtcoderAPI, AtcoderMatcher, AtcoderParser
from .contest_sites.topcoder import TopcoderMatcher
from .contest_sites.yukicoder import YukicoderAPI, YukicoderMatcher, YukicoderParser


class ContestSiteFactory:
    def __init__(self, site_name):
        self.site_name = site_name

    def get_matcher(self):
        if self.site_name == "Atcoder":
            return AtcoderMatcher()
        elif self.site_name == "Yukicoder":
            return YukicoderMatcher()
        elif self.site_name == "Topcoder":
            return TopcoderMatcher()
        # ... 他のコンテストサイトも追加可能
        else:
            raise ValueError(f"Unknown site name: {self.site_name}")

    def get_parser(self):
        if self.site_name == "Atcoder":
            return AtcoderParser()
        elif self.site_name == "Yukicoder":
            return YukicoderParser()
        # ... 他のサイトに関するParserも同様に追加
        else:
            raise ValueError(f"Unknown site name: {self.site_name}")

    def get_api(self):
        if self.site_name == "Atcoder":
            return AtcoderAPI()
        elif self.site_name == "Yukicoder":
            return YukicoderAPI()
        # ... 他のサイトに関するAPIも同様に追加
        else:
            raise ValueError(f"Unknown site name: {self.site_name}")
