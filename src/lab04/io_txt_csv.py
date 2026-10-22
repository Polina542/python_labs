import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    читает текстовый файл целиком и возвращает его содержимое одной строкой

    по умолчанию используется кодировка utf-8, если файл сохранён в другой кодировке, 
    то её можно указать через параметр encoding(например encoding="cp1251")

    FileNotFoundError: если указанный файл не найден
    UnicodeDecodeError: если содержимое нельзя декодировать с использованием указанной кодировки
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''создает/перезаписывает CSV-файл с разделителем-запятой

    если передан header, то он записывается первой строкой

    ValueError: если длины строк не совпадают.
    '''
    p = Path(path)

    expected_length = len(header) if header is not None else None

    for index, row in enumerate(rows):
        if expected_length is None:
            expected_length = len(row)
        elif len(row) != expected_length:
            raise ValueError(
                f"Строка {index + 1} имеет длину {len(row)}, "
                f"ожидалась длина {expected_length}."
            )

    with p.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    '''создает родительские директории для указанного пути, если их нет'''
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
