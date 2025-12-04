from dataclasses import dataclass
from datetime import datetime, date
import re

@dataclass
class Student:
    """
    Класс для представления студента.
    
    Атрибуты:
    ----------
    fio : str
        ФИО студента
    birthdate : str
        Дата рождения в формате ГГГГ-ММ-ДД
    group : str
        Группа студента
    gpa : float
        Средний балл (от 0 до 5)
    """
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """
        Автоматически вызывается после создания объекта.
        Проводит валидацию данных.
        """
        # Валидация формата даты
        try:
            # Пробуем преобразовать строку в дату (формат YYYY-MM-DD)
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Используйте формат YYYY-MM-DD")
        
        # Валидация диапазона среднего балла
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть от 0 до 5, получено: {self.gpa}")
    
    def age(self) -> int:
        """
        Рассчитывает возраст студента на текущую дату.
        
        Возвращает:
        -----------
        int
            Возраст студента в годах
        """
        # Преобразуем строку с датой рождения в объект date
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        # Получаем текущую дату
        today = date.today()
        
        # Вычисляем возраст
        age = today.year - birth_date.year
        
        # Проверяем, был ли уже день рождения в этом году
        # Сравниваем месяц и день
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        """
        Преобразует объект Student в словарь.
        
        Возвращает:
        -----------
        dict
            Словарь с данными студента
        """
        # Правильно сопоставляем поля
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """
        Создает объект Student из словаря.
        
        Параметры:
        ----------
        data : dict
            Словарь с данными студента
        
        Возвращает:
        -----------
        Student
            Объект класса Student
        """
        # ИСПРАВЛЕНО: Правильно создаем объект из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление студента.
        """
        # Возвращаем строку, а не кортеж
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa:.1f}, Возраст: {self.age()}"