def divide_number():
    try:
        user_input = input("Введите число для деления 100: ")
        number = float(user_input)

        if number == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")

        result = 100 / number
        return f"Результат деления 100 на {number} равен {result}"

    except ValueError:
        return "Ошибка: Введите число, а не строку."

    except ZeroDivisionError as ze:
        return f"Ошибка: {ze}"


result_message = divide_number()
print(result_message)