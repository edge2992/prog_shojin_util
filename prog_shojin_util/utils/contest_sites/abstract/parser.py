from abc import ABC, abstractmethod


class ParserInterface(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, url: str) -> dict:
        pass
