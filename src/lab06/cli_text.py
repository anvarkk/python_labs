import argparse
import sys
from pathlib import Path
import re
from collections import Counter

def stats_command(args):
    """
    Анализ частот слов в тексте
    """
    try:
        # Проверяем существование файла
        if not Path(args.input).exists():
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        
        # Читаем файл
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Разбиваем текст на слова 
        words = re.findall(r'\b[а-яa-z]+\b', text.lower())
        
        # Подсчитываем частоты
        word_counts = Counter(words)
        
        # Выводим топ-N слов
        top_n = args.top
        print(f"Топ-{top_n} самых частых слов:")
        print("-" * 30)
        
        for word, count in word_counts.most_common(top_n):
            print(f"{word}: {count}")
            
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def cat_command(args):
    """
    Вывод содержимого файла построчно
    """
    try:
        # Проверяем существование файла
        if not Path(args.input).exists():
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        
        # Читаем и выводим файл
        with open(args.input, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if args.n:  # если включена нумерация
                    print(f"{line_num:>4}: {line}", end='')
                else:
                    print(line, end='')
                    
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Утилиты для работы с текстом')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    
    # Подкоманда stats
    stats_parser = subparsers.add_parser('stats', help='Анализ частот слов в тексте')
    stats_parser.add_argument('--input', required=True, help='Путь к текстовому файлу')
    stats_parser.add_argument('--top', type=int, default=5, help='Количество топ-слов (по умолчанию: 5)')
    
    # Подкоманда cat
    cat_parser = subparsers.add_parser('cat', help='Вывод содержимого файла')
    cat_parser.add_argument('--input', required=True, help='Путь к файлу')
    cat_parser.add_argument('-n', action='store_true', help='Нумерация строк')
    
    args = parser.parse_args()
    
    if args.command == 'stats':
        stats_command(args)
    elif args.command == 'cat':
        cat_command(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()