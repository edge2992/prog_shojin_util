import re
from typing import Optional

from ..abstract import ParsedProblem, ParserInterface


class YukicoderParser(ParserInterface):
    URL_PATTERN = re.compile(r"https://yukicoder\.me/problems/no/(\d+)")

    @classmethod
    def extract_problem_id(cls, url: str) -> Optional[str]:
        match = cls.URL_PATTERN.match(url)
        if match:
            return match.group(1)
        return None

    @classmethod
    def parse(cls, url: str) -> Optional[ParsedProblem]:
        problem_id = cls.extract_problem_id(url)
        if problem_id is None:
            return None

        return ParsedProblem(problem_id=problem_id)
