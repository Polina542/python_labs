m = int(input('Минуты: '))

h = m//60
m = m % 60
print(f'{h}:{m:02d}')
