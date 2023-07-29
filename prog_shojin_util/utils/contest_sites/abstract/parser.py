from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedProblem:
    problem_id: str


class ParserInterface(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, url: str) -> Optional[ParsedProblem]:
        pass
