months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

while True:
    date = input("Дата: ")
    # Правим баг механизма проверки работы
    date = date.replace("-e ","")

    # Проверяем, введенная дата в правильном формате или нет
    if '.' in date:  # Если формат даты "дд.мм.гггг"
        day, month, year = date.split('.')
    else:  # Если формат даты "дд месяц гггг"
        day, month, year = date.split(' ')

    try:
        day = int(day)
        if (month.isdigit()):
            month = int(month)
        else:
            month = months.index(month.lower()) + 1
        year = int(year)

        if 1 <= day <= 31 and 1 <= month <= 12:
            break  # Если дата введена правильно, выходим из цикла
    except (ValueError, IndexError):
        day = 1

# Преобразуем дату в формат гггг-мм-дд
formatted_date = f"{year:04}-{month:02}-{day:02}"
print(f"{formatted_date}")

