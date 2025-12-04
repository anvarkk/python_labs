import json
from pathlib import Path
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.
    
    Параметры:
    ----------
    students : List[Student]
        Список объектов Student
    path : str
        Путь для сохранения JSON файла
    """
    # Преобразуем студентов в словари
    data = [student.to_dict() for student in students]
    
    # Создаем директорию, если она не существует
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем в JSON файл с красивым форматированием
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    
    print(f"Данные сохранены в файл: {path}")

def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON файла.
    
    Параметры:
    ----------
    path : str
        Путь к JSON файлу
    
    Возвращает:
    -----------
    List[Student]
        Список объектов Student
    """
    # Проверяем существование файла
    if not Path(path).exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    # Читаем JSON файл
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Проверяем, что это список
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив объектов")
    
    # Преобразуем словари в объекты Student
    students = []
    for item in data:
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError) as e:
            # Можно добавить логирование ошибки
            print(f"Ошибка при создании студента: {e}")
            raise
    
    return students