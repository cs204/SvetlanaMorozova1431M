def calculate_fuel_percentage(fuel):
    try:
        x, y = map(int, fuel.split('/'))
        if x < 0 or y <= 0 or x > y:
            raise ValueError
        percentage = round((x / y) * 100)

        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f'{percentage}%'
    except ValueError:
        return calculate_fuel_percentage(input("Дробь: "))

    except ZeroDivisionError:
        return calculate_fuel_percentage(input("Дробь: "))

print(calculate_fuel_percentage(input("Дробь: ")))
