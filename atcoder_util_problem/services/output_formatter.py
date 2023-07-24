import pandas as pd
from typing import Optional


class OutputFormatter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def to_json(self) -> Optional[str]:
        return self.df.to_json(orient="records")

    def to_csv(self) -> str:
        return self.df.to_csv()

    def to_markdown(self) -> Optional[str]:
        return self.df.to_markdown()
