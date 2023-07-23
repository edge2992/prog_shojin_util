import requests

BASE_URL = "https://kenkoooo.com/atcoder/atcoder-api/v3"


class AtcoderAPI:
    @staticmethod
    def fetch_submissions(user_id: str, from_second: int) -> list[dict]:
        endpoint = f"{BASE_URL}/user/submissions"
        params = {"user": user_id, "from_second": from_second}

        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            raise Exception("Failed to get submissions")

        return response.json()

    @staticmethod
    def filter_ac_problems(submissions: list[dict]) -> list[dict]:
        ac_problems = [sub for sub in submissions if sub["result"] == "AC"]
        return ac_problems

    @staticmethod
    def remove_duplicate_problems(problems: list[dict]) -> list[dict]:
        seen_problems_ids = set()
        unique_ac_problems = []
        for problem in problems:
            problem_id = problem["problem_id"]
            if problem_id not in seen_problems_ids:
                seen_problems_ids.add(problem_id)
                unique_ac_problems.append(problem)

        return unique_ac_problems

    @staticmethod
    def get_ac_problems(user_id: str, from_second: int) -> list[dict]:
        submissions = AtcoderAPI.fetch_submissions(user_id, from_second)
        ac_problems = AtcoderAPI.filter_ac_problems(submissions)
        unique_ac_problems = AtcoderAPI.remove_duplicate_problems(ac_problems)
        return unique_ac_problems
