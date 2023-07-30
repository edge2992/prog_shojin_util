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

    # 2. OutputFormatterのインスタンスを作成し、そのto_acc_jsonメソッドを呼び出す
    formatter = OutputFormatter(test_data)
    actual_output = formatter.to_acc_json()

    # 3. 期待されるJSON出力とメソッドの実際の出力を比較する
    expected_output = """{
  "contest": {
    "id": "prog_shojin_util",
    "title": "prog_shojin_util",
    "url": "query_url (TODO)"
  },
  "tasks": [
    {
      "id": "abc001_a",
      "label": "0",
      "title": "abc001_a",
      "url": "https://atcoder.jp/contests/abc001/tasks/abc001_a"
    },
    {
      "id": "abc001_b",
      "label": "1",
      "title": "abc001_b",
      "url": "https://atcoder.jp/contests/abc001/tasks/abc001_b"
    }
  ]
}"""

    assert actual_output == expected_output
