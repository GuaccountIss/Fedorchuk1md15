def check_divisible_by_three(number):
    if number % 3 == 0:
        return f"{number} делится на 3 без остатка."
    else:
        return f"{number} не делится на 3 без остатка."

number = int(input("Введите число: "))
result = check_divisible_by_three(number)
print(result)