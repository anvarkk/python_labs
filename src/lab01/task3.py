"""
Задание 3 - Чек: скидка и НДС
Ввод: price (P), discount (%), vat (%) — вещественные
Формулы:
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
Вывод: по строкам, 2 знака после запятой
"""

# Получаем ввод от пользователя
price_input = input("price: ").replace(',', '.')
discount_input = input("discount (%): ").replace(',', '.')
vat_input = input("vat (%): ").replace(',', '.')

# Преобразуем в вещественные числа
price = float(price_input)
discount = float(discount_input)
vat = float(vat_input)

# Вычисляем по формулам
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

# Форматируем вывод с двумя знаками после запятой и символом рубля
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
