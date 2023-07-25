from atcoder_util_problem.scraper.link_collector import LinkCollector
from atcoder_util_problem.utils.contest_sites.abstract import (
    ParserInterface,
)
from atcoder_util_problem.utils.contest_sites.atcoder import AtcoderAPI
from atcoder_util_problem.utils.contest_sites.abstract import APIUtils


class ProblemFinder:
    def __init__(self, parser: ParserInterface):
        self.parser = parser

    def find_problems(
        self,
        user: str,
        target: str,
        status: str,
        from_second: int = 0,
        max_results: int = 500,
    ):
        urls = LinkCollector(target).fetch_links()

        problems = [
            {**parsed, "url": url}
            for url in urls
            if (parsed := self.parser.parse(url)) is not None
            and all(value is not None for value in parsed.values())
        ]

        if status == "both":
            return problems

        ac_problems = APIUtils.get_ac_problems(AtcoderAPI(), user, from_second)
        ac_problem_ids = [problem["problem_id"] for problem in ac_problems]

        if status == "ac":
            return [
                problem
                for problem in problems
                if problem["problem_id"] in ac_problem_ids
            ]
        elif status == "not-ac":
            return [
                problem
                for problem in problems
                if problem["problem_id"] not in ac_problem_ids
            ]
        else:
            raise ValueError(
                "status must be ac, not-ac or both. not {}".format(status)
            )
