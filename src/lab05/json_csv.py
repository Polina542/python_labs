import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    source = Path(json_path)
    destination = Path(csv_path)

    if source.suffix.lower() != ".json":
        raise ValueError("Ожидается файл с расширением .json")

    if destination.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    with source.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not data:
        raise ValueError("JSON должен содержать непустой список словарей")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    fieldnames = sorted({key for item in data for key in item})

    if not fieldnames:
        raise ValueError("В JSON отсутствуют поля для записи в CSV")

    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    source = Path(csv_path)
    destination = Path(json_path)

    if source.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    if destination.suffix.lower() != ".json":
        raise ValueError("Ожидается файл с расширением .json")

    with source.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not any(name is not None and name.strip() for name in reader.fieldnames):
            raise ValueError("В CSV отсутствует заголовок")

        if any(name is None or not name.strip() for name in reader.fieldnames):
            raise ValueError("Заголовки CSV не должны быть пустыми")

        data = list(reader)

    if not data:
        raise ValueError("CSV не содержит строк с данными")

    with destination.open("w", encoding="utf-8", newline="") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
