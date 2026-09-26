name = input('ФИО: ').split()
initials = name[0][0]+name[1][0]+name[2][0]
res = initials.upper()
l = len(name[0])+len(name[1])+len(name[2])+2
print(f'Инициалы: {res}')
print(f'Длина (символов): {l}')
