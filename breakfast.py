menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

order = []

while True:
    try:
        dish = input("Блюдо: ").lower()
        if dish in menu:
            order.append(menu[dish])
    except EOFError:
        break

total = sum(order)
print("")
print(f"Сумма: {total:.2f}")
