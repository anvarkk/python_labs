import json
from pathlib import Path
from .models import Student

def students_to_json(students, path):
    """Сохраняет список студентов в файл JSON."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = [s.to_dict() for s in students]
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    """Читает JSON-файл и возвращает list[Student]."""
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Student.from_dict(item) for item in raw]
