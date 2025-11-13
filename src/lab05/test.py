# src/lab05/test_conversion.py
import os
import sys
from pathlib import Path

# Добавляем текущую директорию в путь для импорта
sys.path.append(os.path.dirname(__file__))

from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

def main():
    # Создаем абсолютные пути относительно этого файла
    base_dir = Path(__file__).parent
    
    # Определяем пути к файлам
    samples_dir = base_dir / "data" / "samples"
    out_dir = base_dir / "data" / "out"
    
    # Создаем папку out если не существует
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Пути к исходным файлам
    people_json = samples_dir / "people.json"
    people_csv = samples_dir / "people.csv"
    cities_csv = samples_dir / "cities.csv"
    
    # Пути к выходным файлам
    people_from_json_csv = out_dir / "people_from_json.csv"
    people_from_csv_json = out_dir / "people_from_csv.json"
    people_xlsx = out_dir / "people.xlsx"
    cities_xlsx = out_dir / "cities.xlsx"
    
    print("Начинаем конвертацию...")
    
    try:
        # Выполняем конвертацию
        json_to_csv(str(people_json), str(people_from_json_csv))
        print("✓ JSON → CSV завершено")
        
        csv_to_json(str(people_csv), str(people_from_csv_json))
        print("✓ CSV → JSON завершено")
        
        csv_to_xlsx(str(people_csv), str(people_xlsx))
        print("✓ CSV → XLSX (people) завершено")
        
        csv_to_xlsx(str(cities_csv), str(cities_xlsx))
        print("✓ CSV → XLSX (cities) завершено")
        
        print(f"\nВсе файлы сохранены в: {out_dir}")
        print("Созданные файлы:")
        for file in out_dir.iterdir():
            print(f"  - {file.name}")
            
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()