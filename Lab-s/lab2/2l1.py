def check_password(password, confirmation):
    if password == confirmation:
        return "Пароль принят"
    else:
        return ""

# Ввод пароля и подтверждения
password = input("Введите пароль: ")
confirmation = input("Подтвердите пароль: ")

# Проверка пароля и вывод результата
result = check_password(password, confirmation)
print(result)