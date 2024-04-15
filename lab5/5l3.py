days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")


num_weekends = int(input("Сколько выходных дней вы хотите на неделе? "))


weekends = days_of_week[-num_weekends:]
workdays = days_of_week[:len(days_of_week) - num_weekends]

# Вывод результатов
print("Ваши выходные дни:", ', '.join(weekends))
print("Ваши рабочие дни:", ', '.join(workdays))