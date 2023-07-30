import json
from datetime import datetime

from prog_shojin_util.cli_config import CliConfig
from prog_shojin_util.services.output_formatter import OutputFormatter


def test_to_acc_json():
    # 1. テストデータを作成する
    test_data = {
        "Atcoder": [
            "https://atcoder.jp/contests/abc001/tasks/abc001_a",
            "https://atcoder.jp/contests/abc001/tasks/abc001_b",
        ],
        "Yukicoder": [
            "https://yukicoder.me/problems/no/2",
        ],
    }
    cli_config = CliConfig(
        atcoder_user="",
        yukicoder_user="",
        target="https://example.com",
        status="not-ac",
        output="acc_json",
        since=datetime(2023, 1, 1),
    )

    # 2. OutputFormatterのインスタンスを作成し、そのto_acc_jsonメソッドを呼び出す
    formatter = OutputFormatter(test_data, cli_config)
    actual_output = formatter.display()
    assert actual_output is not None

    # 3. JSONをPythonの辞書に変換
    actual_dict = json.loads(actual_output)
    expected_dict = {
        "contest": {
            "id": "prog_shojin_util",
            "title": "prog_shojin_util",
            "url": "https://example.com",
        },
        "tasks": [
            {
                "id": "abc001_a",
                "label": "0_abc001_a",
                "title": "abc001_a",
                "url": "https://atcoder.jp/contests/abc001/tasks/abc001_a",
            },
            {
                "id": "abc001_b",
                "label": "1_abc001_b",
                "title": "abc001_b",
                "url": "https://atcoder.jp/contests/abc001/tasks/abc001_b",
            },
        ],
    }

    # 4. 辞書の各キーごとにアサーション
    assert actual_dict["contest"] == expected_dict["contest"]

    for i, (actual_task, expected_task) in enumerate(
        zip(actual_dict["tasks"], expected_dict["tasks"])
    ):
        assert (
            actual_task == expected_task
        ), f"Task at index {i} does not match expected!"
