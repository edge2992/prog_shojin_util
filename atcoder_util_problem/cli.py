import click
from datetime import datetime, timedelta
import pandas as pd
from atcoder_util_problem.utils.contest_sites.atcoder.parser import (
    AtcoderParser,
)
from atcoder_util_problem.services.output_formatter import OutputFormatter
from atcoder_util_problem.services.problem_finder import ProblemFinder


@click.command()
@click.option("-u", "--user", required=True, help="User ID for AtCoder.")
@click.option("-t", "--target", required=True, help="Target URL to process.")
@click.option(
    "--status",
    type=click.Choice(["ac", "not-ac", "both"]),
    default="not-ac",
    help="Filter problems based on the AC status. Default is 'not-ac'.",
)
@click.option(
    "--output",
    type=click.Choice(["json", "markdown", "csv"]),
    default="json",
    help="Output format. Default is 'json'.",
)
@click.option(
    "--since",
    type=click.DateTime(),
    default=(datetime.now() - timedelta(days=182)).strftime("%Y-%m-%d"),
    help="Start datetime to filter problems. The format is 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'. Default is 6 months ago.",
)
@click.option(
    "--max-results",
    type=int,
    default=500,
    help="Maximum number of problems to return. Default is 500.",
)
def find_problems(user, target, status, output, since, max_results):
    """AtCoder Utility Tool for Problems."""
    since = int(datetime.timestamp(since))

    parser = AtcoderParser()
    finder = ProblemFinder(parser)
    problems = finder.find_problems(user, target, status, since, max_results)

    df = pd.DataFrame(problems)
    formatter = OutputFormatter(df)

    if output == "json":
        click.echo(formatter.to_json())
    elif output == "markdown":
        click.echo(formatter.to_markdown())
    elif output == "csv":
        click.echo(formatter.to_csv())
