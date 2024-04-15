
students_languages = {
    'Иван': {'английский', 'французский', 'немецкий'},
    'Мария': {'английский', 'китайский', 'испанский'},
    'Петр': {'немецкий', 'китайский', 'японский'},
    'Анна': {'французский', 'испанский', 'португальский'},
    'Алексей': {'английский', 'испанский'}
}


all_languages = set()

for languages in students_languages.values():
    all_languages.update(languages)


sorted_languages = sorted(all_languages)
print("Список различных языков, которые знают студенты:")
for lang in sorted_languages:
    print(lang)


chinese_speakers = [student for student, languages in students_languages.items() if 'китайский' in languages]
print("\nСтуденты, которые знают китайский язык:")
for student in chinese_speakers:
    print(student)
