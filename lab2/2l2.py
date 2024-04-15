def check_seat_type(seat_number):
    if seat_number % 2 == 0:
        if seat_number <= 36:
            return "Нижнее место в купе"
        else:
            return "Такого места нет"
    else:
        if seat_number <= 36:
            return "Верхнее место в купе"
        else:
            return "Верхнее место в боковом вагоне"

# Ввод номера места
seat_number = int(input("Введите номер места: "))

# Проверка типа места и вывод результата
result = check_seat_type(seat_number)
print(result)