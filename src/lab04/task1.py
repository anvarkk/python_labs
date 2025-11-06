import csv
from pathlib import Path
from typing import Union

def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Читает содержимое текстового файла и возвращает его как одну строку.
    
    """
    with open(path, 'r', encoding=encoding) as file:
        return file.read()

def write_csv(rows: list[Union[tuple, list]], 
              path: Union[str, Path], 
              header: tuple[str, ...] | None = None) -> None:
    """
    Создает или перезаписывает CSV файл с разделителем ','.
    
    """
    # Проверяем одинаковую длину всех строк
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {first_length}")
    
    # Создаем родительские директории если нужно
    ensure_parent_dir(path)
    
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        if header:
            writer.writerow(header)
        
        writer.writerows(rows)

def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создает родительские директории для указанного пути, если они не существуют.
    
    """
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)

# Мини-тесты для проверки функций
if __name__ == "__main__":
    # Тест 1: Чтение текстового файла
    try:
        # Создадим тестовый файл для чтения
        test_input_path = Path("data/input.txt")
        ensure_parent_dir(test_input_path)
        with open(test_input_path, 'w', encoding='utf-8') as f:
            f.write("Тестовый тескт для проверки функций")
        
        txt = read_text("data/input.txt")
        print(f"✓ read_text работает: {txt[:20]}...")
    except Exception as e:
        print(f"✗ read_text ошибка: {e}")
    
    # Тест 2: Запись CSV
    try:
        write_csv([("word", "count"), ("test", 3)], "data/check.csv")
        print("✓ write_csv с заголовком в данных работает")
    except Exception as e:
        print(f"✗ write_csv ошибка: {e}")
    
    # Тест 3: Запись CSV с отдельным заголовком
    try:
        write_csv([("test", 3), ("example", 1)], "data/check2.csv", header=("word", "count"))
        print("✓ write_csv с отдельным header работает")
    except Exception as e:
        print(f"✗ write_csv с header ошибка: {e}")
    
    # Тест 4: Проверка ошибки разной длины строк
    try:
        write_csv([("a", "b"), ("c",)], "data/error.csv")
        print("✗ Должна была быть ошибка разной длины")
    except ValueError as e:
        print(f"✓ Корректно обработана ошибка разной длины: {e}")
    
    # Тест 5: Пустой файл
    try:
        empty_content = read_text("data/empty.txt")
        print(f"✓ Пустой файл работает: '{empty_content}'")
    except FileNotFoundError:
        print("✓ Файл не найден - ожидаемо")
    except Exception as e:
        print(f"✗ Ошибка с пустым файлом: {e}")
    
    print("\nВсе тесты завершены!")