import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    """
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    if not json_file.suffix.lower() == '.json':
        raise ValueError("Файл должен быть в формате JSON")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if len(data) == 0:
        raise ValueError("JSON файл пустой")
    
    # Получаем все уникальные ключи из всех объектов
    all_keys = set()
    for item in data:
        if isinstance(item, dict):
            all_keys.update(item.keys())
    
    fieldnames = sorted(all_keys)  # алфавитный порядок
    
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            if not isinstance(item, dict):
                continue
            # Заполняем отсутствующие поля пустыми строками
            row = {key: item.get(key, '') for key in fieldnames}
            writer.writerow(row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if not csv_file.suffix.lower() == '.csv':
        raise ValueError("Файл должен быть в формате CSV")
    
    data = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append(row)
    
    if len(data) == 0:
        raise ValueError("CSV файл пустой или не содержит данных")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)