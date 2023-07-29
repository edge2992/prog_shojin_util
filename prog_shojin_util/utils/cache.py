import hashlib
import json
import os

CACHE_DIR = os.path.expanduser("~/.cache/prog-shojin-util")


class CacheManager:
    @staticmethod
    def _get_cache_filename(
        class_name: str, method_name: str, params_dict: dict
    ) -> str:
        # 辞書の内容とメソッド名を文字列に変換して結合
        combined_string = (
            class_name + method_name + json.dumps(params_dict, sort_keys=True)
        )

        # ハッシュキーを生成
        hashed_key = hashlib.md5(combined_string.encode()).hexdigest()

        return os.path.join(CACHE_DIR, f"{hashed_key}.json")

    def read(self, class_name: str, method_name: str, params_dict: dict):
        cache_file = self._get_cache_filename(class_name, method_name, params_dict)
        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                return json.load(f)
        return None

    def write(self, class_name, method_name: str, params_dict: dict, data: list):
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        cache_file = self._get_cache_filename(class_name, method_name, params_dict)
        with open(cache_file, "w") as f:
            json.dump(data, f)
