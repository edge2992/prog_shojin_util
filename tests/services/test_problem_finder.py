import pytest

from prog_shojin_util.services.problem_finder import ProblemFinder

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
    return ProblemFinder("Atcoder", [problem["url"] for problem in SAMPLE_PROBLEMS])


@pytest.fixture
def mock_ac_problems(mocker):
    mocker.patch(
        "prog_shojin_util.utils.contest_sites.APIUtils.get_ac_problems",  # noqa E501
        return_value=SAMPLE_PROBLEMS[:2],
    )


def test_find_problems_both_status(problem_finder):
    problems = problem_finder.find_problems("dummy_user", "both")
    assert len(problems) == 4
    print(problems)
    assert problems == [p["url"] for p in SAMPLE_PROBLEMS]


def test_find_problems_ac_status(problem_finder, mock_ac_problems):
    problems = problem_finder.find_problems("dummy_user", "ac")
    assert len(problems) == 2
    assert problems == [p["url"] for p in SAMPLE_PROBLEMS[:2]]


def test_find_problems_not_ac_status(problem_finder, mock_ac_problems):
    problems = problem_finder.find_problems("dummy_user", "not-ac")
    assert len(problems) == 2
    assert problems == [p["url"] for p in SAMPLE_PROBLEMS[2:]]


def test_find_problems_invalid_status(problem_finder):
    with pytest.raises(ValueError):
        problem_finder.find_problems("dummy_user", "invalid_status")
