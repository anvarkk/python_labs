# src/lab05/json_csv.py
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    """
    # Проверка существования файла
    if not Path(json_path).exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError("Неверный формат JSON файла")
    
    # Проверка типа данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if len(data) == 0:
        raise ValueError("JSON файл пустой")
    
    # Получаем все возможные заголовки из всех объектов
    all_headers = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент JSON должен быть словарем")
        all_headers.update(item.keys())
    
    headers = sorted(all_headers)  # Алфавитный порядок
    
    # Создаем папку для выходного файла если её нет
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Записываем в CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        
        for item in data:
            # Заполняем отсутствующие поля пустыми строками
            row = {header: item.get(header, '') for header in headers}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    data = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков")
            
            for row in reader:
                data.append(row)
                
    except csv.Error:
        raise ValueError("Неверный формат CSV файла")
    
    if len(data) == 0:
        raise ValueError("CSV файл пустой или содержит только заголовки")
    
    # Создаем папку для выходного файла если её нет
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Записываем в JSON
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)