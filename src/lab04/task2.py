import argparse
import sys
from pathlib import Path
from collections import Counter
from typing import List, Tuple

# Импортируем функции из task1
from task1 import read_text, write_csv

def normalize_text(text: str) -> str:
    """
    Нормализует текст: приводит к нижнему регистру, заменяет ё на е,
    заменяет управляющие символы на пробелы, схлопывает пробелы.
    """
    if not text:
        return ""
    
    text = text.casefold()
    text = text.replace('ё', 'е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    
    # Схлопываем множественные пробелы
    while '  ' in text:
        text = text.replace('  ', ' ')
    
    return text.strip()

def tokenize(text: str) -> List[str]:
    """
    Токенизирует нормализованный текст на слова.
    """
    import re
    if not text:
        return []
    
    # \w+(?:-\w+)* - слова, возможно с дефисами внутри
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)

def calculate_word_frequencies(tokens: List[str]) -> List[Tuple[str, int]]:
    """
    Подсчитывает частоты слов и сортирует по убыванию частоты
    а при равных частотах по возрастанию слова
    """
    if not tokens:
        return []
    
    counter = Counter(tokens)
    # Сортировка: сначала по убыванию частоты, потом по возрастанию слова
    return sorted(counter.items(), key=lambda x: (-x[1], x[0]))

def print_summary(tokens: List[str], top_words: List[Tuple[str, int]], top_n: int = 5) -> None:
    """
    Выводит краткую статистику в консоль.
    """
    total_words = len(tokens)
    unique_words = len(set(tokens))
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print(f"Топ-{min(top_n, len(top_words))}: {[word for word, count in top_words[:top_n]]}")

def main():
    """Основная функция скрипта."""
    parser = argparse.ArgumentParser(description='Анализ текста и генерация отчета о частотах слов')
    parser.add_argument('--in', dest='input_file', default='data/input.txt',
                       help='Входной текстовый файл (по умолчанию: data/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/report.csv',
                       help='Выходной CSV файл (по умолчанию: data/report.csv)')
    parser.add_argument('--encoding', default='utf-8',
                       help='Кодировка файлов (по умолчанию: utf-8, для Windows: cp1251)')
    parser.add_argument('--top', type=int, default=5,
                       help='Количество слов для топа (по умолчанию: 5)')
    
    args = parser.parse_args()
    
    try:
        # Чтение входного файла
        text = read_text(args.input_file, args.encoding)
        
        # Обработка текста
        normalized_text = normalize_text(text)
        tokens = tokenize(normalized_text)
        
        # Подсчет частот
        word_frequencies = calculate_word_frequencies(tokens)
        
        # Сохранение отчета
        if word_frequencies:
            write_csv(word_frequencies, args.output_file, header=('word', 'count'))
        else:
            # Если слов нет, создаем файл только с заголовком
            write_csv([], args.output_file, header=('word', 'count'))
        
        # Вывод статистики
        print_summary(tokens, word_frequencies, args.top)
        
        print(f"\nОтчет сохранен в: {args.output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input_file}' не найден.")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        print("Попробуйте указать правильную кодировку через --encoding (например, --encoding cp1251)")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()