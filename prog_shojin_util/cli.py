from datetime import datetime

import click

from prog_shojin_util.cli_config import CliConfig
from prog_shojin_util.logging_config import setup_logging
from prog_shojin_util.scraper.link_collector import LinkCollector
from prog_shojin_util.services.output_formatter import OutputFormatter
from prog_shojin_util.services.problem_finder import ProblemFinder


@click.command(
    help="Fetch competitive programming problems based on specified criteria. "
    "You can filter problems from platforms like AtCoder and Yukicoder "
    "based on AC status, date range, and other parameters."
)
@click.option(
    "--atcoder-user",
    default=None,
    help="Specify the User ID for AtCoder to filter problems based on the user's activity.",
)
@click.option(
    "--yukicoder-user",
    default=None,
    help="Specify the User Name for Yukicoder to filter problems based on the user's activity.",
)
@click.option(
    "-t",
    "--target",
    required=True,
    help="The base URL from which problem links will be collected.",
)
@click.option(
    "--status",
    type=click.Choice(["ac", "not-ac", "both"]),
    default="not-ac",
    show_default=True,
    help="Filter the problems based on their AC (Accepted) status. "
    "Choose 'ac' for solved problems, 'not-ac' for unsolved problems, and 'both' for all problems.",
)
@click.option(
    "--output",
    type=click.Choice(["json", "markdown", "csv", "acc_json"]),
    default="json",
    show_default=True,
    help=(
        "Select the output format: "
        "JSON (Standard format), "
        "Markdown (Export in Markdown), "
        "CSV (Export in CSV), "
        "acc_json (Format used by atcoder-cli tool)."
    ),
)
@click.option(
    "--since",
    type=click.DateTime(),
    default="2012-01-01",
    help="Filter problems that were available since the specified date. "
    "Provide the date in 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS' format. By default, it's set to 2012-01-01.",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Enable this option to get detailed logging information, useful for debugging.",
)
def find_problems(
    atcoder_user,
    yukicoder_user,
    target,
    status,
    output,
    since,
    verbose,
):
    """Competitive Programming Utility Tool for Problems Fetching."""
    setup_logging(verbose)

    cli_config = CliConfig(
        atcoder_user=atcoder_user,
        yukicoder_user=yukicoder_user,
        target=target,
        status=status,
        output=output,
        since=since,
    )

    contest_user_data = [
        ("Atcoder", cli_config.atcoder_user),
        ("Yukicoder", cli_config.yukicoder_user),
    ]

    urls = LinkCollector(target).fetch_links()
    since = int(datetime.timestamp(since))
    results = {}  # {contest: [problems]}

    # コンテストごとに問題を取得
    for contest, user in contest_user_data:
        finder = ProblemFinder(contest, urls)
        problems = finder.find_problems(user, status, since, True)
        results[contest] = problems

    formatter = OutputFormatter(results, cli_config)
    click.echo(formatter.display())
