import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует CSV-файл в XLSX.
    Первая строка CSV содержит заголовки.
    Лист называется Sheet1.
    Ширина столбцов подбирается по длине текста,
    но составляет не менее 8 символов.
    Кодировка исходного файла — UTF-8.
    """
    source = Path(csv_path)
    destination = Path(xlsx_path)

    if source.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    if destination.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается файл с расширением .xlsx")

    with source.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows or not any(cell.strip() for row in rows for cell in row):
        raise ValueError("CSV-файл пуст")

    header = rows[0]

    if not header or any(not cell.strip() for cell in header):
        raise ValueError("CSV должен содержать непустые заголовки")

    if any(len(row) != len(header) for row in rows):
        raise ValueError(
            "Количество столбцов в строках не совпадает с заголовком")

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    for row in rows:
        sheet.append(row)

    for column in sheet.columns:
        max_length = max(len(str(cell.value or "")) for cell in column)
        column_letter = column[0].column_letter
        sheet.column_dimensions[column_letter].width = max(8, max_length + 2)

    workbook.save(destination)
    workbook.close()
