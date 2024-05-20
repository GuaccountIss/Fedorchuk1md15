import json


# Функция для чтения данных из JSON файла
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    return data['products']


# Функция для вывода информации о продуктах
def print_product_info(products):
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = product['available']
        availability = "В наличии" if available else "Нет в наличии!"

        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(f"{availability}\n")


# Основная часть программы
file_path = 'F:\Admin\Desktop\products.json'  # Укажите путь к вашему JSON файлу
products = read_json(file_path)
print_product_info(products)
