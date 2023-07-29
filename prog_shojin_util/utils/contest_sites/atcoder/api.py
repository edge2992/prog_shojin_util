import logging
import time

import requests

from prog_shojin_util.utils.cache import CacheManager

from ..abstract import APIInterface

BASE_URL = "https://kenkoooo.com/atcoder/atcoder-api/v3"
logger = logging.getLogger(__name__)


class AtcoderAPI(APIInterface):
    SUBMISSION_LIMIT = 500
    SUBMISSION_ENDPOINT = f"{BASE_URL}/user/submissions"

    def __init__(self):
        self.cache_manager = CacheManager()

    def _read_from_cache(self, user_id: str, from_second: int):
        param_dict = {"user_id": user_id, "from_second": from_second}
        data = self.cache_manager.read(
            self.__class__.__name__, "_fetch_submissions", param_dict
        )

        if data:
            logger.debug(f"Reading cached data for user {user_id}).")
        else:
            logger.debug(f"No cache found for user {user_id}.")
        return data

    def _write_to_cache(self, user_id: str, from_second: int, data: list):
        param_dict = {"user_id": user_id, "from_second": from_second}
        self.cache_manager.write(
            self.__class__.__name__, "_fetch_submissions", param_dict, data
        )
        logger.debug(f"Writing cache for user {user_id}.")

    def _get_submissions_from_api(self, user_id: str, from_second: int) -> list:
        params = {"user": user_id, "from_second": from_second}
        logger.debug(f"Fetching submissions for user {user_id} from {from_second}")
        response = requests.get(self.SUBMISSION_ENDPOINT, params=params)
        response.raise_for_status()

        return response.json()

    def _fetch_submissions(
        self, user_id: str, from_second: int, use_cache: bool
    ) -> list[dict]:
        iter_second = from_second
        all_submissions = []

        if use_cache:
            cached_data = self._read_from_cache(user_id, from_second)
            if cached_data:
                all_submissions.extend(cached_data)
                iter_second = all_submissions[-1]["epoch_second"] + 1

        while True:
            submissions = self._get_submissions_from_api(user_id, iter_second)
            all_submissions.extend(submissions)
            logger.debug(
                f"Received {len(submissions)} submissions. Total so far: {len(all_submissions)}"
            )

            if len(submissions) < self.SUBMISSION_LIMIT:
                logger.debug("No more submissions to fetch")
                break

            iter_second = submissions[-1]["epoch_second"] + 1
            time.sleep(1)

        self._write_to_cache(user_id, from_second, all_submissions)
        return all_submissions

    def _filter_ac_problems(self, submissions: list[dict]) -> list[dict]:
        return [sub for sub in submissions if sub["result"] == "AC"]

    def get_ac_problems(
        self, user: str, from_second: int, use_cache=True
    ) -> list[dict]:
        submissions = self._fetch_submissions(user, from_second, use_cache)
        return self._filter_ac_problems(submissions)

    def get_problem_identifier_key(self) -> str:
        return "problem_id"
