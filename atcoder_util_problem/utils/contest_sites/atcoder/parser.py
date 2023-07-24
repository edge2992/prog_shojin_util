import re
from typing import Optional
from ..abstract_contest import ContestSiteParser


class AtcoderParser(ContestSiteParser):
    # contestsとtasksの部分をキャプチャするための正規表現
    URL_PATTERN = re.compile(
        r"https://atcoder\.jp/contests/(?P<contest_id>[^/]+)/tasks/(?P<problem_id>[^/]+)"
    )

    @classmethod
    def extract_problem_id(cls, url: str) -> Optional[str]:
        match = cls.URL_PATTERN.match(url)
        if match:
            return match.group("problem_id")
        return None

    @classmethod
    def extract_contest_id(cls, url: str) -> Optional[str]:
        match = cls.URL_PATTERN.match(url)
        if match:
            return match.group("contest_id")
        return None
