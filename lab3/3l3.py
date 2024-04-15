# Функция для проверки, является ли слово редким
def is_rare_word(word):
    if 'ф' in word.lower():
        return True
    else:
        return False


# Основная часть программы
while True:
    word = input("Введите слово (для выхода введите 'stop'): ")
    if word == "stop":
        break

    if is_rare_word(word):
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")