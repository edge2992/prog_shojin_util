from .abstract import APIInterface


class APIUtils:
    @staticmethod
    def remove_duplicate_problems(
        api: APIInterface, problems: list[dict]
    ) -> list[dict]:
        problem_identifier_key = api.get_problem_identifier_key()

        seen_problems_ids = set()
        unique_ac_problems = []
        for problem in problems:
            problem_id = problem[problem_identifier_key]
            if problem_id not in seen_problems_ids:
                seen_problems_ids.add(problem_id)
                unique_ac_problems.append(problem)

        return unique_ac_problems

    @staticmethod
    def get_ac_problems(
        api: APIInterface, user: str, from_second: int, use_cache: bool = True
    ) -> list[dict]:
        if user is None:
            return []

        ac_problems = api.get_ac_problems(user, from_second)
        unique_ac_problems = APIUtils.remove_duplicate_problems(api, ac_problems)
        return unique_ac_problems

    @staticmethod
    def get_ac_problems_id_set(
        api: APIInterface, user: str, from_second: int, use_cache: bool = True
    ) -> set[str]:
        unique_ac_problems = APIUtils.get_ac_problems(api, user, from_second)
        ac_problem_ids = set(
            [
                problem[api.get_problem_identifier_key()]
                for problem in unique_ac_problems
            ]
        )
        return ac_problem_ids
