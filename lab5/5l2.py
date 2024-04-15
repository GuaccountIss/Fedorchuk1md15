my_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if duplicates:
    print("Повторяющиеся элементы в списке:", duplicates)
else:
    print("В списке нет повторяющихся элементов.")
