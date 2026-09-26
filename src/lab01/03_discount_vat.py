price = float(input('price='))
discount = float(input('dicsount='))
vat = float(input('vat='))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:>10.2f} ₽')
print(f'НДС:               {vat_amount:>10.2f} ₽')
print(f'Итого к оплате:    {total:>10.2f} ₽')
