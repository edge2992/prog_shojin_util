from dataclasses import dataclass
from typing import Optional

import pandas as pd

from prog_shojin_util.utils.contest_site_factory import ContestSiteFactory
from prog_shojin_util.utils.contest_sites.abstract.parser import ParserInterface


@dataclass
class FormattedProblem:
    contest: str
    problem: Optional[str]
    url: str
    status: Optional[str]


class OutputFormatter:
    parsers: dict[str, ParserInterface] = {}

    def __init__(self, data: dict[str, list]):
        self.df = self._format(data)

    def _get_parser(self, contest) -> ParserInterface:
        if contest in self.parsers:
            return self.parsers[contest]

        factory = ContestSiteFactory(contest)
        self.parsers[contest] = factory.get_parser()
        return self.parsers[contest]

    def _get_problem_name(self, url: str, contest: str) -> Optional[str]:
        parser = self._get_parser(contest)
        parsed_problem = parser.parse(url)
        if parsed_problem is None:
            return None

        return parsed_problem.problem_id

    def _format(self, data: dict[str, list]) -> pd.DataFrame:
        dfs = []
        for contest, urls in data.items():
            formated_problems = [
                FormattedProblem(
                    contest=contest,
                    problem=self._get_problem_name(url, contest),
                    url=url,
                    status="",
                )
                for url in urls
            ]
            df = pd.DataFrame(formated_problems)
            dfs.append(df)

        return pd.concat(dfs)

    def to_json(self) -> Optional[str]:
        return self.df.to_json(orient="records")

    def to_csv(self) -> str:
        return self.df.to_csv()

    def to_markdown(self) -> Optional[str]:
        return self.df.to_markdown()
