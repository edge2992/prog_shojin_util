import hashlib
import json
import time
import requests
import logging
import os

from ..abstract import APIInterface

BASE_URL = "https://kenkoooo.com/atcoder/atcoder-api/v3"
CACHE_DIR = os.path.expanduser("~/.cache/prog-shojin-util")
logger = logging.getLogger(__name__)


class AtcoderAPI(APIInterface):
    SUBMISSION_LIMIT = 500

    def _read_from_cache(self, user_id: str, from_second: int):
        cache_file = self._get_cache_filename(user_id, from_second)
        if os.path.exists(cache_file):
            logger.debug(
                f"Reading cached data for user {user_id} from {cache_file}."
            )
            with open(cache_file, "r") as f:
                return json.load(f)
        logger.debug(f"No cache found for user {user_id} at {cache_file}.")
        return None

    def _write_to_cache(self, user_id: str, from_second: int, data: list):
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
            logger.debug(
                f"Cache directory {CACHE_DIR} not found. Created new one."
            )
        cache_file = self._get_cache_filename(user_id, from_second)
        with open(cache_file, "w") as f:
            json.dump(data, f)
        logger.debug(
            f"Saved data for user {user_id} to cache at {cache_file}."
        )

    @staticmethod
    def _get_cache_filename(user_id: str, from_second: int) -> str:
        hashed_key = hashlib.md5(
            f"{user_id}_{from_second}".encode()
        ).hexdigest()
        return os.path.join(CACHE_DIR, f"{hashed_key}.json")

    def _fetch_submissions(self, user_id: str, from_second: int) -> list[dict]:
        iter_second = from_second
        all_submissions = []

        cached_data = self._read_from_cache(user_id, from_second)
        if cached_data:
            all_submissions.extend(cached_data)
            iter_second = all_submissions[-1]["epoch_second"] + 1

        while True:
            endpoint = f"{BASE_URL}/user/submissions"
            params = {"user": user_id, "from_second": iter_second}
            logger.debug(
                f"Fetching submissions for user {user_id} from {iter_second}"
            )

            response = requests.get(endpoint, params=params)
            response.raise_for_status()

            submissions = response.json()
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

    def get_ac_problems(self, user: str, from_second: int) -> list[dict]:
        submissions = self._fetch_submissions(user, from_second)
        return self._filter_ac_problems(submissions)

    def get_problem_identifier_key(self) -> str:
        return "problem_id"
