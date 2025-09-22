from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Patient:
    id: int
    name: str
    age: int
    diagnosis: Optional[str] = None

    def to_dict(self):
        return asdict(self)
