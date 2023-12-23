def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    v = v.replace("ft", "")  # удаляем "ft" из строки
    v = float(v)  # преобразуем строку в число с плавающей точкой
    v = v * 0.3048  # переводим футы в метры
    return v

main()

