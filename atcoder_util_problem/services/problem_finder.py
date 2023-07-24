from atcoder_util_problem.scraper.link_collector import LinkCollector
from atcoder_util_problem.api.atcoder import AtcoderAPI


class ProblemFinder:
    def __init__(self, parser):
        self.parser = parser

    def find_problems(self, user, target, status, from_second=0):
        urls = LinkCollector(target).fetch_links()

        problems = [
            problem
            for problem in (
                {**self.parser.parse(url), "url": url} for url in urls
            )
            if all(value is not None for value in problem.values())
        ]

        if status == "both":
            return problems

        ac_problems = AtcoderAPI.get_ac_problems(user, from_second)
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
