# Функция для чтения данных из файла и создания русско-английского словаря
def create_ru_en_dict(file_path):
    ru_en_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            en_word, ru_translations = line.strip().split(' - ')
            ru_words = ru_translations.split(', ')

            for ru_word in ru_words:
                if ru_word not in ru_en_dict:
                    ru_en_dict[ru_word] = []
                ru_en_dict[ru_word].append(en_word)

    return ru_en_dict


# Функция для записи русско-английского словаря в файл, отсортированного по ключам
def write_ru_en_dict(file_path, ru_en_dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en_dict.keys()):
            en_words = ', '.join(sorted(ru_en_dict[ru_word]))
            file.write(f"{ru_word} – {en_words}\n")


# Основная часть программы
en_ru_file_path = 'en-ru.txt'  # Путь к входному файлу
ru_en_file_path = 'ru-en.txt'  # Путь к выходному файлу

# Создание русско-английского словаря
ru_en_dict = create_ru_en_dict(en_ru_file_path)

# Запись русско-английского словаря в файл
write_ru_en_dict(ru_en_file_path, ru_en_dict)

print(f"Русско-английский словарь успешно создан в файле {F:\Admin\Desktop\ru-en.txt}.")