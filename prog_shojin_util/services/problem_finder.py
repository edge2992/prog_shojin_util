from typing import Optional

from prog_shojin_util.utils.contest_site_factory import ContestSiteFactory
from prog_shojin_util.utils.contest_sites import APIUtils


class ProblemFinder:
    def __init__(self, site_name: str, urls: list[str]):
        self.factory = ContestSiteFactory(site_name)
        self.parser = self.factory.get_parser()
        self.matcher = self.factory.get_matcher()
        self.api = self.factory.get_api()
        self.urls = urls

    def _get_parsed_problem(self, url: str) -> Optional[str]:
        parsed_problem = self.parser.parse(url)
        if parsed_problem is None:
            return None

        return parsed_problem.problem_id

    def find_problems(
        self,
        user: str,
        status: str,
        from_second: int = 0,
        use_cache: bool = True,
    ) -> list[str]:
        problems = [url for url in self.urls if self.matcher.match(url)]

        if status == "both":
            return problems

        # 対象となるコンテストサイトがないので、空のリストを返す。
        if len(problems) == 0:
            return problems

        ac_problem_ids = APIUtils.get_ac_problems_id_set(
            self.api, user, from_second, use_cache
        )

        if status == "ac":
            return [
                url
                for url in problems
                if self._get_parsed_problem(url) in ac_problem_ids
            ]
        elif status == "not-ac":
            return [
                url
                for url in problems
                if self._get_parsed_problem(url) not in ac_problem_ids
            ]
        else:
            raise ValueError("status must be ac, not-ac or both. not {}".format(status))
