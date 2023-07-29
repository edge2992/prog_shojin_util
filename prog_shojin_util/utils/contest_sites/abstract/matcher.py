import re
from abc import ABC


class MatcherInterface(ABC):
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
