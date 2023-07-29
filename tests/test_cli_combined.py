import pytest
from click.testing import CliRunner
from prog_shojin_util.cli import find_problems
import json


SAMPLE_ATCODER_PROBLEM_LINKS = [
    "https://atcoder.jp/contests/abs/tasks/abc086_a",
    "https://atcoder.jp/contests/abs/tasks/abc086_b",
    "https://atcoder.jp/contests/abs/tasks/abc086_c",
]

SAMPLE_YUKICODER_PROBLEM_LINKS = [
    "https://yukicoder.me/problems/no/1",
    "https://yukicoder.me/problems/no/2",
    "https://yukicoder.me/problems/no/3",
]


SAMPLE_PROBLEM_LINKS = [
    *SAMPLE_ATCODER_PROBLEM_LINKS,
    *SAMPLE_YUKICODER_PROBLEM_LINKS,
]

SAMPLE_ATCODER_AC_PROBLEMS = [
    {"problem_id": "abc086_a"},
    {"problem_id": "abc086_b"},
]

SAMPLE_YUKICODER_AC_PROBLEMS = [
    {"No": "1"},
    {"No": "2"},
]


@pytest.fixture
def mock_fetch_links(mocker):
    return mocker.patch(
        "prog_shojin_util.scraper.link_collector.LinkCollector.fetch_links",  # noqa : E501
        return_value=SAMPLE_PROBLEM_LINKS,
    )


@pytest.fixture
def mock_get_ac_problems_atcoder(mocker):
    return mocker.patch(
        "prog_shojin_util.utils.contest_sites.atcoder.AtcoderAPI.get_ac_problems",  # noqa: E501
        return_value=SAMPLE_ATCODER_AC_PROBLEMS,
    )


@pytest.fixture
def mock_get_ac_problems_yukicoder(mocker):
    return mocker.patch(
        "prog_shojin_util.utils.contest_sites.yukicoder.YukicoderAPI.get_ac_problems",  # noqa: E501
        return_value=SAMPLE_YUKICODER_AC_PROBLEMS,
    )


def test_find_ac_problems_cli_combined(
    mock_fetch_links,
    mock_get_ac_problems_atcoder,
    mock_get_ac_problems_yukicoder,
):
    runner = CliRunner()

    # yukicoderとatcoder両方の問題を検索するためのオプション
    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user_yukicoder",
            "--atcoder-user",
            "dummy_user_atcoder",
            "-t",
            "https://target_blog_url",
            "--status",
            "not-ac",
        ],
    )

    result_json = json.loads(result.output)
    result_problems = [problem["problem"] for problem in result_json]

    assert result.exit_code == 0

    assert len(result_json) == len(SAMPLE_PROBLEM_LINKS) - len(
        SAMPLE_ATCODER_AC_PROBLEMS
    ) - len(SAMPLE_YUKICODER_AC_PROBLEMS)

    # yukicoderの問題が正しく出力されているか確認
    assert "1" not in result_problems
    assert "2" not in result_problems
    assert "3" in result_problems

    # atcoderの問題が正しく出力されているか確認
    assert "abc086_a" not in result_problems
    assert "abc086_b" not in result_problems
    assert "abc086_c" in result_problems


def test_find_ac_problems_cli_only_yukicoder(
    mock_fetch_links,
    mock_get_ac_problems_yukicoder,
):
    runner = CliRunner()

    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user_yukicoder",
            "-t",
            "https://target_blog_url",
            "--status",
            "not-ac",
        ],
    )

    result_json = json.loads(result.output)
    result_problems = [problem["problem"] for problem in result_json]

    assert result.exit_code == 0
    assert "1" not in result_problems
    assert "2" not in result_problems
    assert "3" in result_problems

    assert "abc086_a" in result_problems
    assert "abc086_b" in result_problems
    assert "abc086_c" in result_problems


def test_find_ac_problems_cli_only_atcoder(
    mock_fetch_links,
    mock_get_ac_problems_atcoder,
):
    runner = CliRunner()

    result = runner.invoke(
        find_problems,
        [
            "--atcoder-user",
            "dummy_user_atcoder",
            "-t",
            "https://target_blog_url",
            "--status",
            "not-ac",
        ],
    )

    result_json = json.loads(result.output)
    result_problems = [problem["problem"] for problem in result_json]

    assert result.exit_code == 0
    assert "abc086_a" not in result_problems
    assert "abc086_b" not in result_problems
    assert "abc086_c" in result_problems

    assert "1" in result_problems
    assert "2" in result_problems
    assert "3" in result_problems


def test_find_ac_problems_cli_no_user_option(
    mock_fetch_links,
):
    runner = CliRunner()

    result = runner.invoke(
        find_problems,
        [
            "-t",
            "https://target_blog_url",
            "--status",
            "not-ac",
        ],
    )

    result_json = json.loads(result.output)
    result_problems = [problem["problem"] for problem in result_json]

    assert result.exit_code == 0

    assert "1" in result_problems
    assert "2" in result_problems
    assert "3" in result_problems

    assert "abc086_a" in result_problems
    assert "abc086_b" in result_problems
    assert "abc086_c" in result_problems
