amount_due = 50
coin = 0

while coin < amount_due:
    print(f"Нужная сумма: {amount_due}")
    coin = int(input("Вставьте монету: "))

change_owed = coin - amount_due
print(f"Ваша сдача: {change_owed}")
