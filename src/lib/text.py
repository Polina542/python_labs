# 1

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''приводит строку к casefold, заменяет ё на е,заменяет управляющие символы \t, \r, \n на пробел, \
        меняет несколько пробелов на один, убирает пробелы по бокам'''
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    control_chars = {chr(i) for i in range(32)} | {'\u007f'}

    chars = []
    for ch in text:
        if ch in control_chars:
            chars.append(" ")
        else:
            chars.append(ch)

    text = "".join(chars)
    text = " ".join(text.split())

    return text


# 2
import re


def tokenize(text: str) -> list[str]:
    '''разбивает строку на «слова» по небуквенно-цифровым разделителям'''
    pattern = r'\w+(?:-\w+)*'
    return [match.group() for match in re.finditer(pattern, text)]


# 3

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''считает частоты, возвращает словарь слово → количество'''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


# 4

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова'''
    if not isinstance(freq, dict):
        raise ValueError("Первый аргумент должен быть словарём.")

    if not all(isinstance(v, int) for v in freq.values()):
        raise ValueError("Значения в словаре должны быть целыми числами.")

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

# print(count_freq(["a", "b", "a", "c", "b", "a"]))
# print(count_freq(["bb", "aa", "bb", "aa", "cc"]))

print(top_n({"a": 3, "b": 2, "c": 1}, n=2))
print(top_n({"aa": 2, "bb": 2, "cc": 1}, n=2))
