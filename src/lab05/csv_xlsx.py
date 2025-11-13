import csv
from pathlib import Path
import openpyxl
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if not csv_file.suffix.lower() == '.csv':
        raise ValueError("Файл должен быть в формате CSV")
    
    # Читаем CSV
    data = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    
    if len(data) == 0:
        raise ValueError("CSV файл пустой")
    
    # Создаем Excel файл
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"
    
    # Записываем данные
    for row_idx, row_data in enumerate(data, 1):
        for col_idx, value in enumerate(row_data, 1):
            sheet.cell(row=row_idx, column=col_idx, value=value)
    
    # Настраиваем авто-ширину колонок
    for column_cells in sheet.columns:
        length = 8  # минимальная ширина
        for cell in column_cells:
            if cell.value:
                length = max(length, len(str(cell.value)))
        sheet.column_dimensions[get_column_letter(column_cells[0].column)].width = length + 2
    
    workbook.save(xlsx_path)