import pytest
from click.testing import CliRunner
from prog_shojin_util.cli import find_problems


@pytest.fixture
def mock_fetch_links(mocker):
    return mocker.patch(
        "prog_shojin_util.scraper.link_collector.LinkCollector.fetch_links",  # noqa : E501
        return_value=[
            "https://atcoder.jp/contests/abs/tasks/abc086_a",
            "https://atcoder.jp/contests/abs/tasks/abc086_b",
            "https://atcoder.jp/contests/abs/tasks/abc086_c",
        ],
    )


@pytest.fixture
def mock_get_ac_problems(mocker):
    return mocker.patch(
        "prog_shojin_util.utils.contest_sites.APIUtils.get_ac_problems",  # noqa: E501
        return_value=[
            {"problem_id": "abc086_a"},
            {"problem_id": "abc086_b"},
        ],
    )


def test_find_ac_problems_cli(mock_fetch_links, mock_get_ac_problems):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--atcoder-user",
            "dummy_user",
            "-t",
            "https://atcoder.jp/contests/abs",
            "--status",
            "ac",
        ],
    )

    assert result.exit_code == 0
    assert "abc086_a" in result.output
    assert "abc086_b" in result.output
    # abc086_cは"ac"になっていないため
    assert "abc086_c" not in result.output


# 以下のテストは"not-ac"のステータスを持つ問題を検索します。
def test_find_not_ac_problems_cli(mock_fetch_links, mock_get_ac_problems):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--atcoder-user",
            "dummy_user",
            "-t",
            "https://atcoder.jp/contests/abs",
            "--status",
            "not-ac",
        ],
    )

    assert result.exit_code == 0
    assert "abc086_a" not in result.output
    assert "abc086_b" not in result.output
    # abc086_cは"ac"になっていないため
    assert "abc086_c" in result.output


# 以下のテストは"both"のステータスを持つ問題を検索します。
def test_find_both_problems_cli(mock_fetch_links, mock_get_ac_problems):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--atcoder-user",
            "dummy_user",
            "-t",
            "https://atcoder.jp/contests/abs",
            "--status",
            "both",
        ],
    )
    assert result.exit_code == 0
    assert "abc086_a" in result.output
    assert "abc086_b" in result.output
    assert "abc086_c" in result.output


# 以下のテストはCSV出力オプションを持つ問題を検索します。
def test_csv_output_problems_cli(mock_fetch_links, mock_get_ac_problems):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--atcoder-user",
            "dummy_user",
            "-t",
            "https://atcoder.jp/contests/abs",
            "--status",
            "ac",
            "--output",
            "csv",
        ],
    )

    assert result.exit_code == 0
    # CSV形式の出力が正しいか確認します。
    assert "abc086_a" in result.output
