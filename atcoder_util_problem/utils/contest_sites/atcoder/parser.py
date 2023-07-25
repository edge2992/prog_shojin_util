import re
from typing import Optional
from ..abstract import ParserInterface


class AtcoderParser(ParserInterface):
    # contestsとtasksの部分をキャプチャするための正規表現
    URL_PATTERN = re.compile(
        r"https://atcoder\.jp/contests/(?P<contest_id>[^/]+)/tasks/(?P<problem_id>[^/]+)"  # noqa: E501
    )

    @classmethod
    def extract_problem_id(cls, url: str) -> Optional[str]:
        """URLからproblem_idを抽出する"""
        match = cls.URL_PATTERN.match(url)
        if match:
            return match.group("problem_id")
        return None

    @classmethod
    def extract_contest_id(cls, url: str) -> Optional[str]:
        """URLからcontest_idを抽出する"""
        match = cls.URL_PATTERN.match(url)
        if match:
            return match.group("contest_id")
        return None

    @classmethod
    def parse(cls, url: str) -> dict:
        """URLからcontest_idとproblem_idを抽出する"""
        return {
            "problem_id": cls.extract_problem_id(url),
            "contest_id": cls.extract_contest_id(url),
        }
