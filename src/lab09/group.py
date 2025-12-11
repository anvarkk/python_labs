# src/lab09/group.py
import csv
from pathlib import Path
import sys

# Исправляем импорт: добавляем путь к src
sys.path.insert(0, str(Path(__file__).parent.parent))

# Теперь импорт сработает
from lab08.models import Student


class Group:
    """
    Класс для работы с группой студентов.
    Сохраняет студентов в CSV файле как в базе данных.
    """
    
    def __init__(self, csv_file_path):
        """
        Создаем группу студентов.
        
        Args:
            csv_file_path (str): Путь к CSV файлу с данными студентов
        """
        self.csv_path = Path(csv_file_path)
        self._make_sure_file_exists()
    
    def _make_sure_file_exists(self):
        """Создает CSV файл с заголовками, если его нет."""
        if not self.csv_path.exists():
            # Создаем папку, если ее нет
            self.csv_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Создаем файл и записываем заголовки
            with open(self.csv_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_students_from_file(self):
        """Читает всех студентов из CSV файла."""
        students = []
        
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Проверяем, что в файле правильные заголовки
            headers = reader.fieldnames
            if headers != ['fio', 'birthdate', 'group', 'gpa']:
                raise ValueError("Неправильный формат CSV файла!")
            
            # Читаем каждую строку
            for row in reader:
                try:
                    # Создаем студента из данных строки
                    student = Student(
                        fio=row['fio'],
                        birthdate=row['birthdate'],
                        group=row['group'],
                        gpa=float(row['gpa'])
                    )
                    students.append(student)
                except Exception as e:
                    print(f"Ошибка в строке: {row}. Пропускаем. Ошибка: {e}")
        
        return students
    
    def _save_students_to_file(self, students):
        """Сохраняет всех студентов в CSV файл."""
        with open(self.csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            
            for student in students:
                # Преобразуем студента в словарь для записи
                student_dict = {
                    'fio': student.fio,
                    'birthdate': student.birthdate,
                    'group': student.group,
                    'gpa': student.gpa
                }
                writer.writerow(student_dict)
    
    def add(self, student):
        """
        Добавляет нового студента в группу.
        
        Args:
            student (Student): Студент для добавления
        """
        # Получаем всех студентов
        all_students = self._read_students_from_file()
        
        # Проверяем, нет ли уже такого студента
        for s in all_students:
            if s.fio.lower() == student.fio.lower():
                raise ValueError(f"Студент {student.fio} уже есть в группе!")
        
        # Добавляем нового студента
        all_students.append(student)
        
        # Сохраняем обратно в файл
        self._save_students_to_file(all_students)
        print(f"✓ Добавлен: {student.fio}")
    
    def list(self):
        """
        Возвращает список всех студентов.
        
        Returns:
            list: Список студентов в группе
        """
        return self._read_students_from_file()
    
    def find(self, search_text):
        """
        Ищет студентов по имени.
        
        Args:
            search_text (str): Текст для поиска в ФИО
            
        Returns:
            list: Найденные студенты
        """
        all_students = self._read_students_from_file()
        found = []
        
        search_text = search_text.lower()
        
        for student in all_students:
            if search_text in student.fio.lower():
                found.append(student)
        
        return found
    
    def remove(self, student_name):
        """
        Удаляет студента по имени.
        
        Args:
            student_name (str): ФИО студента для удаления
            
        Returns:
            bool: True если удалили, False если не нашли
        """
        all_students = self._read_students_from_file()
        old_count = len(all_students)
        
        # Оставляем только тех, кого не нужно удалять
        new_students = []
        for student in all_students:
            if student.fio.lower() != student_name.lower():
                new_students.append(student)
        
        # Если количество изменилось - значит кого-то удалили
        if len(new_students) < old_count:
            self._save_students_to_file(new_students)
            print(f"✓ Удален: {student_name}")
            return True
        else:
            print(f"✗ Не найден: {student_name}")
            return False
    
    def update(self, student_name, **changes):
        """
        Изменяет данные студента.
        
        Args:
            student_name (str): ФИО студента для изменения
            **changes: Что изменить, например: group='ИСП-202', gpa=4.5
            
        Returns:
            bool: True если изменили, False если не нашли
        """
        all_students = self._read_students_from_file()
        changed = False
        
        for i, student in enumerate(all_students):
            if student.fio.lower() == student_name.lower():
                # Копируем данные студента
                student_data = {
                    'fio': student.fio,
                    'birthdate': student.birthdate,
                    'group': student.group,
                    'gpa': student.gpa
                }
                
                # Обновляем указанные поля
                for key, value in changes.items():
                    if key in student_data:
                        student_data[key] = value
                        print(f"  Изменено {key} на {value}")
                
                # Создаем нового студента с обновленными данными
                new_student = Student(**student_data)
                all_students[i] = new_student
                changed = True
        
        if changed:
            self._save_students_to_file(all_students)
            print(f"✓ Обновлен: {student_name}")
            return True
        else:
            print(f"✗ Не найден для обновления: {student_name}")
            return False
    
    def count(self):
        """Сколько студентов в группе."""
        return len(self._read_students_from_file())
    
    def show_all(self):
        """Показывает всех студентов красиво."""
        students = self.list()
        if not students:
            print("В группе нет студентов")
            return
        
        print(f"Всего студентов: {len(students)}")
        print("-" * 60)
        for i, student in enumerate(students, 1):
            print(f"{i:2}. {student.fio:30} | {student.group:10} | GPA: {student.gpa} | Возраст: {student.age()}")
        print("-" * 60)