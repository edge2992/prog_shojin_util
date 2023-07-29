import pytest
from click.testing import CliRunner
from prog_shojin_util.cli import find_problems

# Yukicoder用のモックデータ
SAMPLE_YUKICODER_LINKS = [
    "https://yukicoder.me/problems/no/1",
    "https://yukicoder.me/problems/no/2",
    "https://yukicoder.me/problems/no/3",
]

SAMPLE_YUKICODER_AC_PROBLEMS = [
    {"No": "1"},
    {"No": "2"},
]


@pytest.fixture
def mock_fetch_links_yukicoder(mocker):
    return mocker.patch(
        "prog_shojin_util.scraper.link_collector.LinkCollector.fetch_links",
        return_value=SAMPLE_YUKICODER_LINKS,
    )


@pytest.fixture
def mock_get_ac_problems_yukicoder(mocker):
    return mocker.patch(
        "prog_shojin_util.utils.contest_sites.APIUtils.get_ac_problems",
        return_value=SAMPLE_YUKICODER_AC_PROBLEMS,
    )


def test_find_ac_problems_cli_yukicoder(
    mock_fetch_links_yukicoder, mock_get_ac_problems_yukicoder
):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user",
            "-t",
            "https://yukicoder.me/problems",
            "--status",
            "ac",
        ],
    )

    assert result.exit_code == 0
    assert "1" in result.output
    assert "2" in result.output
    assert "3" not in result.output


def test_find_not_ac_problems_cli_yukicoder(
    mock_fetch_links_yukicoder, mock_get_ac_problems_yukicoder
):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user",
            "-t",
            "https://yukicoder.me/problems",
            "--status",
            "not-ac",
        ],
    )

    assert result.exit_code == 0
    assert "1" not in result.output
    assert "2" not in result.output
    assert "3" in result.output


def test_find_both_problems_cli_yukicoder(
    mock_fetch_links_yukicoder, mock_get_ac_problems_yukicoder
):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user",
            "-t",
            "https://yukicoder.me/problems",
            "--status",
            "both",
        ],
    )

    assert result.exit_code == 0
    assert "1" in result.output
    assert "2" in result.output
    assert "3" in result.output


def test_csv_output_problems_cli_yukicoder(
    mock_fetch_links_yukicoder, mock_get_ac_problems_yukicoder
):
    runner = CliRunner()
    result = runner.invoke(
        find_problems,
        [
            "--yukicoder-user",
            "dummy_user",
            "-t",
            "https://yukicoder.me/problems",
            "--status",
            "ac",
            "--output",
            "csv",
        ],
    )

    assert result.exit_code == 0
    # YukicoderのCSV形式の出力が正しいか確認します。
    # 実際のCSVのフォーマットに合わせてテストを変更する必要があります。
    assert ",1," in result.output
    assert ",2," in result.output
