# tuples.py

from typing import Tuple


def format_record(rec: Tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("record must be tuple (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("пустое ФИО")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("пустая группа")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    parts = fio.split()  # split() уже убирает лишние пробелы
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать как минимум фамилию и имя")

    surname = parts[0].lower().capitalize()
    names = parts[1:3]  # 1–2 имени для инициалов
    initials = "".join((n[0].upper() + ".") for n in names if n)

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


if __name__ == "__main__":
    cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
        # несколько негативных для демонстрации
        ("", "G-1", 4.0),
        ("Иванов", "G-1", 4.0),
        ("Иванов Иван", "", 4.0),
        ("Иванов Иван", "G-1", "badgpa"),
    ]

    print("format_record")
    for rec in cases:
        try:
            out = format_record(rec)
            print(f"{rec!r} -> {out!r}")
        except Exception as e:
            print(f"{rec!r} -> {type(e).__name__}: {e}")
