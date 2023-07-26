import requests
from ..abstract import APIInterface

BASE_URL = "https://yukicoder.me/api/v1"


class YukicoderAPI(APIInterface):
    def _get_user_id_from_name(self, user_name: str):
        endpoint = f"{BASE_URL}/users/name/{user_name}"
        headers = {"accept": "application/json"}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        user_data = response.json()
        return user_data["Id"]

    def fetch_submissions(
        self, user_name: str, from_second: int
    ) -> list[dict]:
        user_id = self._get_user_id_from_name(user_name)
        endpoint = f"{BASE_URL}/solved/id/{user_id}"
        headers = {"accept": "application/json"}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def filter_ac_problems(self, submissions: list[dict]) -> list[dict]:
        return submissions

    def get_problem_id_key(self) -> str:
        # because No is used in the URL
        # use No as problem_id_key instead of problem_id,
        return "No"  # or No
