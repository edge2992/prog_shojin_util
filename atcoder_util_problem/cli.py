import click
from datetime import datetime, timedelta
import pandas as pd
from atcoder_util_problem.scraper.link_collector import LinkCollector
from atcoder_util_problem.services.output_formatter import OutputFormatter
from atcoder_util_problem.services.problem_finder import ProblemFinder


@click.command()
@click.option("--atcoder-user", default=None, help="User ID for AtCoder.")
@click.option(
    "--yukicoder-user", default=None, help="User Name for Yukicoder."
)
@click.option("-t", "--target", required=True, help="Target URL to process.")
@click.option(
    "--status",
    type=click.Choice(["ac", "not-ac", "both"]),
    default="not-ac",
    show_default=True,
    help="Filter problems based on the AC status.",
)
@click.option(
    "--output",
    type=click.Choice(["json", "markdown", "csv"]),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.option(
    "--since",
    type=click.DateTime(),
    default=(datetime.now() - timedelta(days=182)).strftime("%Y-%m-%d"),
    help="Start datetime to filter problems. The format is 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'. Default is 6 months ago.",  # noqa: E501
)
@click.option(
    "--max-results",
    type=int,
    default=500,
    show_default=True,
    help="Maximum number of problems to return.",
)
def find_problems(
    atcoder_user, yukicoder_user, target, status, output, since, max_results
):
    """AtCoder Utility Tool for Problems."""
    contest_user_data = [
        ("Atcoder", atcoder_user),
        # ("Yukicoder", yukicoder_user),
    ]

    urls = LinkCollector(target).fetch_links()
    since = int(datetime.timestamp(since))
    dfs: list[pd.DataFrame] = []

    for contest, user in contest_user_data:
        finder = ProblemFinder(contest, urls)
        problems = finder.find_problems(user, status, since, max_results)
        dfs.append(pd.DataFrame(problems))

    df = pd.concat(dfs, ignore_index=True)
    formatter = OutputFormatter(df)

    if output == "json":
        click.echo(formatter.to_json())
    elif output == "markdown":
        click.echo(formatter.to_markdown())
    elif output == "csv":
        click.echo(formatter.to_csv())
