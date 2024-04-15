def mix_colors(color1, color2):
    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        return "фиолетовый"
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        return "оранжевый"
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        return "зеленый"
    elif color1 == "красный" and color2 == "красный" or color1 == "красный" and color2 == "красный ":
        return "красный"
    else:
        return "Ошибка! Введите только названия 'красный', 'синий' или 'желтый'."

# Ввод названий цветов
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

# Проверка названий цветов и вывод результата
result = mix_colors(color1, color2)
print(result)