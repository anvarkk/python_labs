import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует CSV файл в XLSX с автоматической шириной колонок.
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    workbook = Workbook()
    worksheet = workbook.active
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            
    except csv.Error:
        raise ValueError("Неверный формат CSV файла")
    
    if len(rows) == 0:
        raise ValueError("CSV файл пустой")
    
    # Записываем данные в XLSX
    for row_idx, row in enumerate(rows, 1):
        for col_idx, value in enumerate(row, 1):
            worksheet.cell(row=row_idx, column=col_idx, value=value)
    
    # Автоматическая ширина колонок
    for column_cells in worksheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        worksheet.column_dimensions[get_column_letter(column_cells[0].column)].width = length + 2
    
    # Создаем папку для выходного файла если её нет
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    
    workbook.save(xlsx_path)