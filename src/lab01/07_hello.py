s = input('in: ')

word = ''
letter1 = 0
letter2 = 0
for i in range(len(s)):
    if s[i] == s[i].upper() and len(word) == 0:
        word += s[i]
        letter1 = i
    if len(word) == 1 and s[i] in '0123456789':
        word += s[i+1]
        letter2 = i+1
        break

d = letter2-letter1
for i in range(letter2+d, len(s), d):
    word += s[i]
    if s[i] == '.':
        break

print(f'out: {word}')
