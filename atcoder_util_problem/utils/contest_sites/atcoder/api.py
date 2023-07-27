import requests

from ..abstract import APIInterface

BASE_URL = "https://kenkoooo.com/atcoder/atcoder-api/v3"


class AtcoderAPI(APIInterface):
    def _fetch_submissions(self, user_id: str, from_second: int) -> list[dict]:
        endpoint = f"{BASE_URL}/user/submissions"
        params = {"user": user_id, "from_second": from_second}

        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        return response.json()

    def _filter_ac_problems(self, submissions: list[dict]) -> list[dict]:
        return [sub for sub in submissions if sub["result"] == "AC"]

    def get_ac_problems(self, user: str, from_second: int) -> list[dict]:
        submissions = self._fetch_submissions(user, from_second)
        return self._filter_ac_problems(submissions)

    def get_problem_identifier_key(self) -> str:
        return "problem_id"
