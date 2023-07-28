import pytest
import requests
from unittest.mock import Mock
from prog_shojin_util.utils.contest_sites.yukicoder import YukicoderAPI


# モック用のデータ
SAMPLE_USER = {"Id": 12345}

SAMPLE_PROBLEMS = [
    {
        "No": 8,
        "ProblemId": 26,
        "Title": "N言っちゃダメゲーム",
        "AuthorId": 10,
        "TesterIds": "",
        "Level": 2,
        "ProblemType": 0,
        "Tags": "発想,動的計画法,メモ化再帰",
        "Date": "2022-09-14T08:47:57+09:00",
    },
    {
        "No": 76,
        "ProblemId": 154,
        "Title": "回数の期待値で練習",
        "AuthorId": 8,
        "TesterIds": "",
        "Level": 3,
        "ProblemType": 0,
        "Tags": "数学,確率,期待値,二分探索,動的計画法",
        "Date": "2022-09-05T23:08:24+09:00",
    },
]


@pytest.fixture
def mock_get_user_id_from_name(monkeypatch):
    def mock_get_user_id(*args, **kwargs):
        return SAMPLE_USER["Id"]

    monkeypatch.setattr(
        YukicoderAPI, "_get_user_id_from_name", mock_get_user_id
    )


@pytest.fixture
def mock_request_get(monkeypatch):
    def mock_get(*args, **kwargs):
        mock_response = Mock(spec=requests.Response)
        if "users/name/" in args[0]:
            mock_response.json.return_value = SAMPLE_USER
        elif "solved/id/" in args[0]:
            mock_response.json.return_value = SAMPLE_PROBLEMS
        return mock_response

    monkeypatch.setattr(requests, "get", mock_get)


def test_get_user_id_from_name(mock_request_get):
    api = YukicoderAPI()
    user_id = api._get_user_id_from_name("sample_user")
    assert user_id == SAMPLE_USER["Id"]


def test_get_ac_problems(mock_get_user_id_from_name, mock_request_get):
    api = YukicoderAPI()
    problems = api.get_ac_problems("sample_user", 123456)
    assert len(problems) == 2
    problem_nos = [problem["No"] for problem in problems]
    assert problems[0]["No"] in problem_nos
    assert problems[1]["No"] in problem_nos


def test_get_problem_identifier_key():
    api = YukicoderAPI()
    key = api.get_problem_identifier_key()
    assert key == "No"
