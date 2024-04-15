
numbers = [15, 27, 8, 42, 5]


user_number = int(input("Пожалуйста, введите число: "))


if user_number in numbers:
    print("Исходный список:", numbers)
    print("Ваше число:", user_number)
    print("Поздравляю, Вы угадали число!")
else:
    print("Исходный список:", numbers)
    print("Ваше число:", user_number)
    print("Нет такого числа!")