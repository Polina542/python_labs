price = float(input('price='))
discount = float(input('dicsount='))
vat = float(input('vat='))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

# print(f'База после скидки: 900.00 ₽')
# # НДС:               180.00 ₽
# # Итого к оплате:    1080.00 ₽
