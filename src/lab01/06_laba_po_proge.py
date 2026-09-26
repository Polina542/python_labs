n = int(input('in_1: '))

a = 0
b = 0
for i in range(n):
    l = input(f'in_{2+i}: ').split()
    if l[-1] == 'True':
        a += 1
    else:
        b += 1

print(f'out: {a} {b}')
