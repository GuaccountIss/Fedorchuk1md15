def create_ru_en_dict(input_file, output_file):
    en_ru_dict = {}
    ru_en_dict = {}


    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            en_word, ru_words = line.strip().split(' - ')
            ru_words_list = [word.strip() for word in ru_words.split(',')]
            en_ru_dict[en_word] = ru_words_list


    for en_word, ru_words_list in en_ru_dict.items():
        for ru_word in ru_words_list:
            if ru_word in ru_en_dict:
                ru_en_dict[ru_word].append(en_word)
            else:
                ru_en_dict[ru_word] = [en_word]


    with open(output_file, 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en_dict.keys()):
            en_words = ', '.join(ru_en_dict[ru_word])
            file.write(f"{ru_word} – {en_words}\n")


input_file = 'en-ru.txt'
output_file = 'ru-en.txt'


create_ru_en_dict(input_file, output_file)