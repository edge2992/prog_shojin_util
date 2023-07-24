import click
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
    help="Filter problems based on the AC status.",
)
@click.option(
    "--output",
    type=click.Choice(["json", "markdown", "csv"]),
    default="json",
    help="Output format.",
)
def find_problems(user, target, status, output):
    """AtCoder Utility Tool for Problems."""
    parser = AtcoderParser()
    finder = ProblemFinder(parser)
    problems = finder.find_problems(user, target, status)

    df = pd.DataFrame(problems)
    formatter = OutputFormatter(df)

    if output == "json":
        click.echo(formatter.to_json())
    elif output == "markdown":
        click.echo(formatter.to_markdown())
    elif output == "csv":
        click.echo(formatter.to_csv())
