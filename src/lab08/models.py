from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str   # ожидаем "YYYY-MM-DD"
    group: str
    gpa: float = 0.0

    def __post_init__(self):
        # простая проверка fio и group
        if not isinstance(self.fio, str) or not self.fio.strip():
            raise ValueError("fio должен быть непустой строкой")
        if not isinstance(self.group, str) or not self.group.strip():
            raise ValueError("group должен быть непустой строкой")

        # проверка формата даты
        if not isinstance(self.birthdate, str):
            raise ValueError("birthdate должен быть строкой 'YYYY-MM-DD'")
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except Exception:
            raise ValueError("Неверный формат birthdate, нужно 'YYYY-MM-DD'")

        # gpa -> float и диапазон
        try:
            self.gpa = float(self.gpa)
        except Exception:
            raise ValueError("gpa должен быть числом")
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa должен быть в диапазоне 0..5")

    def age(self, on_date: date | None = None) -> int:
        """Вернуть полные годы на дату on_date (по умолчанию — сегодня)."""
        if on_date is None:
            on_date = date.today()
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        years = on_date.year - b.year
        if (on_date.month, on_date.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self):
        """Сериализация в словарь (под JSON)."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d):
        """Создаёт Student из словаря."""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return f"{self.fio} — {self.group} — {self.birthdate} — GPA: {self.gpa:.2f}"
