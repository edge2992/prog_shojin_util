import pytest
from atcoder_util_problem.utils.contest_sites.atcoder import AtcoderParser
from atcoder_util_problem.services.problem_finder import ProblemFinder


SAMPLE_PROBLEMS = [
    {
        "problem_id": "abc086_a",
        "contest_id": "abs",
        "url": "https://atcoder.jp/contests/abs/tasks/abc086_a",
    },
    {
        "problem_id": "abc081_a",
        "contest_id": "abs",
        "url": "https://atcoder.jp/contests/abs/tasks/abc081_a",
    },
    {
        "problem_id": "arc065_a",
        "contest_id": "abs",
        "url": "https://atcoder.jp/contests/abs/tasks/arc065_a",
    },
    {
        "problem_id": "arc089_a",
        "contest_id": "abs",
        "url": "https://atcoder.jp/contests/abs/tasks/arc089_a",
    },
]


@pytest.fixture
def problem_finder(mocker):
    return ProblemFinder(AtcoderParser())


@pytest.fixture
def mock_link_collector(mocker):
    mocker.patch(
        "atcoder_util_problem.scraper.link_collector.LinkCollector.fetch_links",  # noqa E501
        return_value=[problem["url"] for problem in SAMPLE_PROBLEMS],
    )


@pytest.fixture
def mock_ac_problems(mocker):
    mocker.patch(
        "atcoder_util_problem.utils.contest_sites.abstract.APIUtils.get_ac_problems",  # noqa E501
        return_value=SAMPLE_PROBLEMS[:2],
    )


def test_find_problems_both_status(problem_finder, mock_link_collector):
    problems = problem_finder.find_problems(
        "dummy_user", "dummy_target", "both"
    )
    assert len(problems) == 4
    print(problems)
    assert [problem["problem_id"] for problem in problems] == [
        p["problem_id"] for p in SAMPLE_PROBLEMS
    ]


def test_find_problems_ac_status(
    problem_finder, mock_link_collector, mock_ac_problems
):
    problems = problem_finder.find_problems("dummy_user", "dummy_target", "ac")
    assert len(problems) == 2
    assert [problem["problem_id"] for problem in problems] == [
        p["problem_id"] for p in SAMPLE_PROBLEMS[:2]
    ]


def test_find_problems_not_ac_status(
    problem_finder, mock_link_collector, mock_ac_problems
):
    problems = problem_finder.find_problems(
        "dummy_user", "dummy_target", "not-ac"
    )
    assert len(problems) == 2
    assert [problem["problem_id"] for problem in problems] == [
        p["problem_id"] for p in SAMPLE_PROBLEMS[2:]
    ]


def test_find_problems_invalid_status(problem_finder, mock_link_collector):
    with pytest.raises(ValueError):
        problem_finder.find_problems(
            "dummy_user", "dummy_target", "invalid_status"
        )
