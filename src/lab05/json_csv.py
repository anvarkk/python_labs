import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    """
    # Проверка существования файла
    if not Path(json_path).exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    # Создание директории для выходного файла если не существует
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Чтение JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError("Неверный формат JSON файла")
    
    # Проверка типа данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    
    if not data:
        raise ValueError("JSON файл пустой")
    
    # Получение всех уникальных ключей (полей)
    all_keys = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Элементы JSON должны быть словарями")
        all_keys.update(item.keys())
    
    # Сортировка ключей по алфавиту
    fieldnames = sorted(all_keys)
    
    # Запись CSV
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                # Заполняем отсутствующие поля пустыми строками
                row = {key: str(item.get(key, '')) for key in fieldnames}
                writer.writerow(row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Создание директории для выходного файла если не существует
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    
    data = []
    
    # Чтение CSV
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            # Сначала попробуем прочитать первую строку как заголовки
            first_line = csv_file.readline().strip()
            if not first_line:
                raise ValueError("CSV файл пустой")
            
            # Проверяем, есть ли запятые в первой строке (признак заголовков)
            if ',' not in first_line:
                raise ValueError("CSV файл не содержит заголовков")
            
            # Возвращаемся к началу файла
            csv_file.seek(0)
            
            reader = csv.DictReader(csv_file)
            
            # Проверка наличия заголовков
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков")
            
            for row in reader:
                # Все значения сохраняются как строки
                data.append(row)
                
    except csv.Error:
        raise ValueError("Неверный формат CSV файла")
    
    if not data:
        raise ValueError("CSV файл пустой (только заголовки)")
    
    # Запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")