from .api import APIInterface


class APIUtils:
    @staticmethod
    def remove_duplicate_problems(
        api: APIInterface, problems: list[dict]
    ) -> list[dict]:
        problem_id_key = api.get_problem_id_key()

        seen_problems_ids = set()
        unique_ac_problems = []
        for problem in problems:
            problem_id = problem[problem_id_key]
            if problem_id not in seen_problems_ids:
                seen_problems_ids.add(problem_id)
                unique_ac_problems.append(problem)

        return unique_ac_problems

    @staticmethod
    def get_ac_problems(
        api: APIInterface, user_id: str, from_second: int
    ) -> list[dict]:
        submissions = api.fetch_submissions(user_id, from_second)
        ac_problems = api.filter_ac_problems(submissions)
        unique_ac_problems = APIUtils.remove_duplicate_problems(
            api, ac_problems
        )
        return unique_ac_problems
