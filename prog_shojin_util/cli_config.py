from dataclasses import dataclass
from datetime import datetime


@dataclass
class CliConfig:
    atcoder_user: str
    yukicoder_user: str
    target: str
    status: str
    output: str
    since: datetime
