import click


@click.command()
@click.option("-u", "--user", required=True, help="Username for AtCoder.")
@click.option(
    "-t", "--target", required=True, help="Target domain to search problems."
)
def find_not_solved_problems(user, target):
    click.echo(
        f"Searching for unsolved problems for user {user} on {target}..."
    )
    # 以下に実際の処理を追加する
