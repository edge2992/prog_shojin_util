from abc import ABC, abstractmethod


class APIInterface(ABC):
    @abstractmethod
    def fetch_submissions(self, user_id: str, from_second: int) -> list[dict]:
        pass

    @abstractmethod
    def filter_ac_problems(self, submissions: list[dict]) -> list[dict]:
        pass

    @abstractmethod
    def get_problem_id_key(self) -> str:
        pass
