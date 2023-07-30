import json
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from prog_shojin_util.cli_config import CliConfig
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

    def __init__(self, data: dict[str, list], cli_config: CliConfig):
        self.df: pd.DataFrame = self._format(data)
        self.config: CliConfig = cli_config

    def display(self) -> Optional[str]:
        if self.config.output == "json":
            return self._to_json()
        elif self.config.output == "csv":
            return self._to_csv()
        elif self.config.output == "markdown":
            return self._to_markdown()
        elif self.config.output == "acc_json":
            return self._to_acc_json()
        else:
            raise ValueError(f"Unexpected output format: {self.config.output}")

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

    def _to_json(self) -> Optional[str]:
        return self.df.to_json(orient="records", indent=2)

    def _to_csv(self) -> str:
        return self.df.to_csv()

    def _to_markdown(self) -> Optional[str]:
        return self.df.to_markdown()

    def _to_acc_json(self) -> Optional[str]:
        # 基本的な出力構造を作成
        result = {"contest": {"id": None, "title": None, "url": None}, "tasks": []}

        result["contest"]["id"] = "prog_shojin_util"
        result["contest"]["title"] = "prog_shojin_util"
        result["contest"]["url"] = self.config.target

        # DataFrameの各行に対してタスク情報を作成
        for index, row in self.df.query("contest == 'Atcoder'").iterrows():
            task = {
                "id": row["problem"],
                "label": f"{index}_{row['problem']}",
                "title": row["problem"],
                "url": row["url"],
            }
            result["tasks"].append(task)

        return json.dumps(result, indent=2)
