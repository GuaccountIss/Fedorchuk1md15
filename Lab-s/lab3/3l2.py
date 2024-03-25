# Инициализация пустой строки
result = ""

# Цикл для ввода и объединения слов
while True:
    word = input("Введите слово (для остановки введите 'stop'): ")
    if word == "stop":
        break
    result += word + " "

# Вывод объединенной строки
print("Результат:", result.strip())