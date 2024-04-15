def is_magic_date(date):
    day, month, year = map(int, date.split('.'))
    if day * month == year % 100:
        return True
    else:
        return False

user_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(user_date):
    print(f"Дата {user_date} является магической!")
else:
    print(f"Дата {user_date} не является магической.")