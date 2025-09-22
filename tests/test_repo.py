import tempfile
from hospital.repo import InMemoryRepo


def test_add_and_list():
    repo = InMemoryRepo()
    p = repo.add_patient('Alice', 30, 'Flu')
    assert p.id == 1
    lst = repo.list_patients()
    assert len(lst) == 1
    assert lst[0].name == 'Alice'


def test_save_and_load(tmp_path):
    repo = InMemoryRepo()
    repo.add_patient('Bob', 45, 'Cold')
    f = tmp_path / 'data.json'
    repo.save(str(f))

    repo2 = InMemoryRepo()
    repo2.load(str(f))
    lst = repo2.list_patients()
    assert len(lst) == 1
    assert lst[0].name == 'Bob'
