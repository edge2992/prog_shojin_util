import click
import json
from atcoder_util_problem.scraper.link_collector import LinkCollector
from atcoder_util_problem.utils.contest_sites.atcoder.parser import (
    AtcoderParser,
)
from atcoder_util_problem.utils.contest_sites.classifier import (
    classify_urls_by_contest_sites,
)
from .api.atcoder import AtcoderAPI


def to_markdown(problems):
    """問題をMarkdown形式で返します。"""
    markdown_list = ["## AtCoder Problems"]
    for problem in problems:
        markdown_list.append(
            f"- [{problem['contest_id']} : {problem['problem_id']}]({problem['url']})"
        )
    return "\n".join(markdown_list)


def to_csv(problems):
    """問題をCSV形式で返します。"""
    csv_list = ["contest_id,problem_id,url"]
    for problem in problems:
        csv_list.append(
            f"{problem['contest_id']},{problem['problem_id']},{problem['url']}"
        )
    return "\n".join(csv_list)


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
    ac_problems = AtcoderAPI.get_ac_problems(user, 0)
    print("ac_problems count: ", len(ac_problems))
    ac_problem_ids = set([problem["problem_id"] for problem in ac_problems])

    lc = LinkCollector(target)
    urls = lc.fetch_links()

    problem_urls = classify_urls_by_contest_sites(urls)
    atcoder_urls = problem_urls["atcoder"]
    atcoder_problems = [
        problem
        for problem in (
            {**AtcoderParser.get_contest_and_problem_id(url), "url": url}
            for url in atcoder_urls
        )
        if all(value is not None for value in problem.values())
    ]

    if status == "ac":
        atcoder_problems = [
            problem
            for problem in atcoder_problems
            if problem["problem_id"] in ac_problem_ids
        ]
    elif status == "not-ac":
        atcoder_problems = [
            problem
            for problem in atcoder_problems
            if problem["problem_id"] not in ac_problem_ids
        ]

    if output == "json":
        click.echo(json.dumps(atcoder_problems, indent=4))
    elif output == "markdown":
        click.echo(to_markdown(atcoder_problems))
    elif output == "csv":
        click.echo(to_csv(atcoder_problems))
