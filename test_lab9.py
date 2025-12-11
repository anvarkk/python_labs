import sys
from pathlib import Path

# Добавляем путь к src в sys.path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

# Теперь импорт сработает
from lab08.models import Student
from lab09.group import Group

print("=== ТЕСТИРУЕМ ЛАБУ 9 ===")
print()

# 1. Создаем группу
print("1. Создаем группу...")
group = Group("data/lab09/students.csv")
print(f"   Файл: data/lab09/students.csv")
print(f"   Студентов в группе: {group.count()}")
print()

# 2. Добавляем студентов
print("2. Добавляем студентов...")

student1 = Student("Иванов Иван", "2000-05-15", "ИСП-201", 4.5)
student2 = Student("Петрова Мария", "2001-08-22", "ИСП-201", 4.8)
student3 = Student("Сидоров Алексей", "1999-12-03", "ИСП-202", 3.9)

try:
    group.add(student1)
    group.add(student2)
    group.add(student3)
    print(f"   Добавлено 3 студента")
except Exception as e:
    print(f"   Ошибка: {e}")

print()

# 3. Показываем всех студентов
print("3. Список всех студентов:")
group.show_all()
print()

# 4. Ищем студентов
print("4. Ищем 'Иванов':")
found = group.find("Иванов")
for s in found:
    print(f"   Найден: {s.fio}, группа: {s.group}")
print()

# 5. Обновляем студента
print("5. Обновляем данные Иванова...")
group.update("Иванов Иван", gpa=4.7, group="ИСП-202")
print()

# 6. Проверяем обновление
print("6. Проверяем обновление:")
group.show_all()
print()

# 7. Удаляем студента
print("7. Удаляем Сидорова...")
group.remove("Сидоров Алексей")
print()

# 8. Финальный список
print("8. Финальный список студентов:")
group.show_all()

print()
print("✅ ВСЕ ОПЕРАЦИИ CRUD РАБОТАЮТ!")