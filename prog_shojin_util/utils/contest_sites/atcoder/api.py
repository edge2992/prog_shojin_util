import time
import requests
import logging

from ..abstract import APIInterface

BASE_URL = "https://kenkoooo.com/atcoder/atcoder-api/v3"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AtcoderAPI(APIInterface):
    SUBMISSION_LIMIT = 500

    def _fetch_submissions(self, user_id: str, from_second: int) -> list[dict]:
        all_submissions = []

        while True:
            endpoint = f"{BASE_URL}/user/submissions"
            params = {"user": user_id, "from_second": from_second}
            logger.info(
                f"Fetching submissions for user {user_id} from {from_second}"
            )

            response = requests.get(endpoint, params=params)
            response.raise_for_status()

            submissions = response.json()
            all_submissions.extend(submissions)
            logger.info(
                f"Received {len(submissions)} submissions. Total so far: {len(all_submissions)}"
            )

            if len(submissions) < self.SUBMISSION_LIMIT:
                logger.info("No more submissions to fetch")
                break

            from_second = submissions[-1]["epoch_second"] - 1
            time.sleep(1)

        return all_submissions

    def _filter_ac_problems(self, submissions: list[dict]) -> list[dict]:
        return [sub for sub in submissions if sub["result"] == "AC"]

    def get_ac_problems(self, user: str, from_second: int) -> list[dict]:
        submissions = self._fetch_submissions(user, from_second)
        return self._filter_ac_problems(submissions)

    def get_problem_identifier_key(self) -> str:
        return "problem_id"
