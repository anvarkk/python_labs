# tests/test_json_csv.py
import pytest
import json
import csv
import sys
from pathlib import Path

# Добавляем путь к src для импорта модулей
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lab05.json_csv import json_to_csv, csv_to_json

def test_json_to_csv_basic(tmp_path):
    """Тест конвертации JSON в CSV - позитивный сценарий"""
    # Создаем временный JSON файл
    json_data = [
        {"name": "Анна", "age": 25, "city": "Москва"},
        {"name": "Иван", "age": 30, "city": "Санкт-Петербург"}
    ]
    
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "output.csv"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f)
    
    # Конвертируем
    json_to_csv(str(json_file), str(csv_file))
    
    # Проверяем результат
    assert csv_file.exists()
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Проверяем количество записей
        assert len(rows) == 2
        # Проверяем заголовки
        assert set(rows[0].keys()) == {"age", "city", "name"}
        # Проверяем данные
        assert rows[0]["name"] == "Анна"
        assert rows[0]["age"] == "25"
        assert rows[1]["city"] == "Санкт-Петербург"

def test_csv_to_json_basic(tmp_path):
    """Тест конвертации CSV в JSON - позитивный сценарий"""
    # Создаем временный CSV файл
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "output.json"
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerow({"name": "Анна", "age": "25", "city": "Москва"})
        writer.writerow({"name": "Иван", "age": "30", "city": "Санкт-Петербург"})
    
    # Конвертируем
    csv_to_json(str(csv_file), str(json_file))
    
    # Проверяем результат
    assert json_file.exists()
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        # Проверяем количество записей
        assert len(data) == 2
        # Проверяем структуру данных
        assert data[0]["name"] == "Анна"
        assert data[0]["age"] == "25"
        assert data[1]["city"] == "Санкт-Петербург"

def test_json_to_csv_missing_fields(tmp_path):
    """Тест конвертации JSON в CSV - отсутствующие поля"""
    json_data = [
        {"name": "Анна", "age": 25},
        {"name": "Иван", "city": "Москва"}
    ]
    
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "output.csv"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f)
    
    json_to_csv(str(json_file), str(csv_file))
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Проверяем что все поля есть, даже если некоторые отсутствовали
        assert set(rows[0].keys()) == {"age", "city", "name"}
        # Отсутствующие поля должны быть пустыми
        assert rows[0]["city"] == ""
        assert rows[1]["age"] == ""

def test_json_to_csv_file_not_found():
    """Тест конвертации JSON в CSV - файл не существует"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")

def test_csv_to_json_file_not_found():
    """Тест конвертации CSV в JSON - файл не существует"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")

def test_json_to_csv_invalid_json(tmp_path):
    """Тест конвертации JSON в CSV - некорректный JSON"""
    json_file = tmp_path / "invalid.json"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write("это не json")
    
    with pytest.raises(ValueError, match="Неверный формат JSON"):
        json_to_csv(str(json_file), "output.csv")

def test_json_to_csv_empty_json(tmp_path):
    """Тест конвертации JSON в CSV - пустой JSON"""
    json_file = tmp_path / "empty.json"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump([], f)
    
    with pytest.raises(ValueError, match="JSON файл пустой"):
        json_to_csv(str(json_file), "output.csv")

def test_csv_to_json_empty_csv(tmp_path):
    """Тест конвертации CSV в JSON - пустой CSV (только заголовки)"""
    csv_file = tmp_path / "empty.csv"
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
    
    with pytest.raises(ValueError, match="CSV файл пустой"):
        csv_to_json(str(csv_file), "output.json")

def test_csv_to_json_no_headers(tmp_path):
    """Тест конвертации CSV в JSON - нет заголовков"""
    csv_file = tmp_path / "no_headers.csv"
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        f.write("Анна,25\nИван,30\n")
    
    with pytest.raises(ValueError, match="CSV файл не содержит заголовков"):
        csv_to_json(str(csv_file), "output.json")