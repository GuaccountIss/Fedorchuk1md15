countries_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Китай": "Пекин",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Япония": "Токио",
    "Великобритания": "Лондон",
    "Италия": "Рим",
    "Канада": "Оттава",
    "Индия": "Нью-Дели"
}

for country, capital in countries_capitals.items():
    print(country, "-", capital)


country = 'Россия'
print("Столица", country, ":", countries_capitals.get(country))


sorted_countries = sorted(countries_capitals.keys())
for country in sorted_countries:
    print(country, "-", countries_capitals[country])