def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return f"Год {year} - високосный"
    else:
        return "Это год не високосный"

# Ввод года
year = int(input("Введите год: "))

# Проверка года и вывод результата
result = leap_year(year)
print(result)