from abc import ABC, abstractmethod


class APIInterface(ABC):
    @abstractmethod
    def get_ac_problems(
        self, user: str, from_second: int, use_cache: bool = True
    ) -> list[dict]:
        pass

    @abstractmethod
    def get_problem_identifier_key(self) -> str:
        pass
