# 1
from re import *


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''...'''

    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е')

    control_chars = set("\t\n\r\f\v" + "".join(chr(i)
                        for i in range(32)) + "\u007f")  # управляющие символы

    chars = []
    for ch in text:
        if ch in control_chars:
            chars.append(" ")
        else:
            chars.append(ch)
    text = "".join(chars)

# 2


def tokenize(text: str) -> list[str]:
    reg = r'\w+(?:-\w+)*'
    l = []

    for x in finditer(reg, text):
        l.append(x.group())

    return l

# 3


def count_freq(tokens: list[str]) -> dict[str, int]:
    for token in tokens:


////тут надо использовать словари
