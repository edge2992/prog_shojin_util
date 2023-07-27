import pytest
from atcoder_util_problem.utils.contest_sites.atcoder import AtcoderAPI
from atcoder_util_problem.utils.contest_sites.abstract import APIUtils

# モック用のデータ
SAMPLE_SUBMISSIONS = [
    {"result": "AC", "problem_id": "abc121_c"},
    {"result": "WA", "problem_id": "abc121_b"},
    {"result": "AC", "problem_id": "abc121_c"},
    {"result": "AC", "problem_id": "abc122_a"},
]


@pytest.fixture
def mock_fetch_submissions(monkeypatch):
    def mock_fetch(*args, **kwargs):
        return SAMPLE_SUBMISSIONS

    monkeypatch.setattr(AtcoderAPI, "_fetch_submissions", mock_fetch)


def test_filter_ac_problems():
    ac_problems = AtcoderAPI()._filter_ac_problems(SAMPLE_SUBMISSIONS)
    assert len(ac_problems) == 3
    assert all(problem["result"] == "AC" for problem in ac_problems)


def test_remove_duplicate_problems():
    ac = AtcoderAPI()
    problems = ac._filter_ac_problems(SAMPLE_SUBMISSIONS)
    unique_problems = APIUtils.remove_duplicate_problems(ac, problems)
    assert len(unique_problems) == 2
    problem_ids = [problem["problem_id"] for problem in unique_problems]
    assert "abc121_c" in problem_ids
    assert "abc122_a" in problem_ids


def test_get_ac_problems(mock_fetch_submissions):
    ac = AtcoderAPI()
    problems = APIUtils.get_ac_problems(ac, "chokudai", 1560046356)
    assert len(problems) == 2
    problem_ids = [problem["problem_id"] for problem in problems]
    assert "abc121_c" in problem_ids
    assert "abc122_a" in problem_ids
