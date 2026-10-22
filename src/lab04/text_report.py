import sys

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir


def main():
    input_path = "data/lab04/input.txt"
    output_path = "data/lab04/report.csv"
    encoding = "utf-8"

    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "--in" and i + 1 < len(args):
            input_path = args[i + 1]
            i += 2
        elif args[i] == "--out" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        elif args[i] == "--encoding" and i + 1 < len(args):
            encoding = args[i + 1]
            i += 2
        else:
            print(f"Неизвестный или неполный аргумент: {args[i]}")
            return

    try:
        raw_text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return
    except UnicodeDecodeError:
        print("Ошибка: неверная кодировка файла")
        return

    tokens = tokenize(normalize(raw_text))
    freq = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(freq)

    all_rows = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    top5 = top_n(freq, n=5)

    ensure_parent_dir(output_path)
    write_csv(all_rows, output_path, header=("word", "count"))

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")

    for word, count in top5:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
