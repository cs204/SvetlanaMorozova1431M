def to_snake_case(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

camel_case = input("Верблюжий стиль: ")
snake_case = to_snake_case(camel_case)

print(snake_case)
