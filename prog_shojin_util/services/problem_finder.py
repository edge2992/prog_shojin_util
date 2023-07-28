from prog_shojin_util.utils.contest_site_factory import ContestSiteFactory
from prog_shojin_util.utils.contest_sites.abstract import APIUtils


class ProblemFinder:
    def __init__(self, site_name: str, urls: list[str]):
        self.factory = ContestSiteFactory(site_name)
        self.parser = self.factory.get_parser()
        self.api = self.factory.get_api()
        self.urls = urls

    def find_problems(
        self,
        user: str,
        status: str,
        from_second: int = 0,
        max_results: int = 500,
    ):
        problems = [
            {**parsed, "url": url}
            for url in self.urls
            if (parsed := self.parser.parse(url)) is not None
            and all(value is not None for value in parsed.values())
        ]

        if status == "both":
            return problems

        # 対象となるコンテストサイトがないので、空のリストを返す。
        if len(problems) == 0:
            return problems

        ac_problems = APIUtils.get_ac_problems(self.api, user, from_second)
        ac_problem_ids = [
            problem[self.api.get_problem_identifier_key()]
            for problem in ac_problems
        ]

        if status == "ac":
            return [
                problem
                for problem in problems
                if problem[self.api.get_problem_identifier_key()]
                in ac_problem_ids
            ]
        elif status == "not-ac":
            return [
                problem
                for problem in problems
                if problem[self.api.get_problem_identifier_key()]
                not in ac_problem_ids
            ]
        else:
            raise ValueError(
                "status must be ac, not-ac or both. not {}".format(status)
            )
