import json
from pathlib import Path
from typing import List

from .models import Patient


class InMemoryRepo:
    def __init__(self):
        self._patients = []
        self._next_id = 1

    def add_patient(self, name: str, age: int, diagnosis: str = None) -> Patient:
        p = Patient(id=self._next_id, name=name, age=age, diagnosis=diagnosis)
        self._patients.append(p)
        self._next_id += 1
        return p

    def list_patients(self) -> List[Patient]:
        return list(self._patients)

    def save(self, path: str):
        data = [p.to_dict() for p in self._patients]
        Path(path).write_text(json.dumps({"patients": data}, indent=2), encoding="utf-8")

    def load(self, path: str):
        p = Path(path)
        if not p.exists():
            return
        doc = json.loads(p.read_text(encoding="utf-8"))
        self._patients = [Patient(**d) for d in doc.get("patients", [])]
        if self._patients:
            self._next_id = max(p.id for p in self._patients) + 1
        else:
            self._next_id = 1
