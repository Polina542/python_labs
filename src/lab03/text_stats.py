import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(base_dir, "lib"))

from text import *

s = sys.stdin.read()

tablitsa = input("таблица(True или False): ").strip().lower()

s_norm = normalize(s)
s_token = tokenize(s_norm)
freq = count_freq(s_token)
top5 = top_n(freq, 5)

print(f'Всего слов: {len(s_token)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')

if tablitsa == 'false':
    for token in top5:
        print(f'{token[0]}:{token[1]}')

elif tablitsa == 'true':
    max_len = max((len(w) for w, _ in top5), default=5)
    header_word = 'слово'.ljust(max_len)

    print()
    print(f'{header_word} | частота')
    print('-' * (max_len + 10))
    for word, count in top5:
        print(f'{word.ljust(max_len)} | {count}')
