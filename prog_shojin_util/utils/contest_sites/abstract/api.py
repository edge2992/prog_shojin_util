from abc import ABC, abstractmethod


class APIInterface(ABC):
    """This class serves as the base interface for API-related operations.

    Note: It is an abstract class and should not be instantiated directly.
    """

    @abstractmethod
    def get_ac_problems(
        self, user: str, from_second: int, use_cache: bool = True
    ) -> list[dict]:
        pass

    @abstractmethod
    def get_problem_identifier_key(self) -> str:
        pass
