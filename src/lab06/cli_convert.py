import argparse
import sys
from pathlib import Path

def json2csv_command(args):
    """
    Конвертация JSON в CSV
    """
    try:
        # Импортируем функции из lab05
        from lab05.json_csv import json_to_csv
        
        # Проверяем существование входного файла
        if not Path(args.infile).exists():
            raise FileNotFoundError(f"Входной файл не найден: {args.infile}")
        
        # Создаем директорию для выходного файла если нужно
        Path(args.outfile).parent.mkdir(parents=True, exist_ok=True)
        
        # Выполняем конвертацию
        json_to_csv(args.infile, args.outfile)
        print(f"Успешно: {args.infile} → {args.outfile}")
        
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        sys.exit(1)

def csv2json_command(args):
    """
    Конвертация CSV в JSON
    """
    try:
        from lab05.json_csv import csv_to_json
        
        if not Path(args.infile).exists():
            raise FileNotFoundError(f"Входной файл не найден: {args.infile}")
            
        Path(args.outfile).parent.mkdir(parents=True, exist_ok=True)
        csv_to_json(args.infile, args.outfile)
        print(f"Успешно: {args.infile} → {args.outfile}")
        
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        sys.exit(1)

def csv2xlsx_command(args):
    """
    Конвертация CSV в XLSX
    """
    try:
        from lab05.csv_xlsx import csv_to_xlsx
        
        if not Path(args.infile).exists():
            raise FileNotFoundError(f"Входной файл не найден: {args.infile}")
            
        Path(args.outfile).parent.mkdir(parents=True, exist_ok=True)
        csv_to_xlsx(args.infile, args.outfile)
        print(f"Успешно: {args.infile} → {args.outfile}")
        
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Конвертация между форматами данных')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    
    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser('json2csv', help='Конвертация JSON в CSV')
    json2csv_parser.add_argument('--in', dest='infile', required=True, help='Входной JSON файл')
    json2csv_parser.add_argument('--out', dest='outfile', required=True, help='Выходной CSV файл')
    
    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser('csv2json', help='Конвертация CSV в JSON')
    csv2json_parser.add_argument('--in', dest='infile', required=True, help='Входной CSV файл')
    csv2json_parser.add_argument('--out', dest='outfile', required=True, help='Выходной JSON файл')
    
    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser('csv2xlsx', help='Конвертация CSV в XLSX')
    csv2xlsx_parser.add_argument('--in', dest='infile', required=True, help='Входной CSV файл')
    csv2xlsx_parser.add_argument('--out', dest='outfile', required=True, help='Выходной XLSX файл')
    
    args = parser.parse_args()
    
    if args.command == 'json2csv':
        json2csv_command(args)
    elif args.command == 'csv2json':
        csv2json_command(args)
    elif args.command == 'csv2xlsx':
        csv2xlsx_command(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()