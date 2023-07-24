from abc import ABC, abstractmethod
import re


class ContestSiteMatcher(ABC):
    _pattern: str = ""
    _key_name: str = ""
    _compiled_pattern = None

    @classmethod
    def _get_compiled_pattern(cls):
        if cls._compiled_pattern is None:
            cls._compiled_pattern = re.compile(cls._pattern)
        return cls._compiled_pattern

    @classmethod
    def match(cls, url: str) -> bool:
        return bool(cls._get_compiled_pattern().match(url))


class ContestSiteParser(ABC):
    @classmethod
    @abstractmethod
    def extract_problem_id(cls, url: str) -> str:
        """URLからproblem_idを抽出する"""
        pass

    @classmethod
    @abstractmethod
    def extract_contest_id(cls, url: str) -> str:
        """URLからcontest_idを抽出する"""
        pass

    @classmethod
    def get_contest_and_problem_id(cls, url: str) -> dict:
        """URLからcontest_idとproblem_idを抽出する"""
        return {
            "problem_id": cls.extract_problem_id(url),
            "contest_id": cls.extract_contest_id(url),
        }
