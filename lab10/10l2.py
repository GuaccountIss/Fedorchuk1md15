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

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    return data['products']


# Функция для записи данных в JSON файл
def write_json(file_path, products):
    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump({"products": products}, jsonfile, ensure_ascii=False, indent=4)


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


# Функция для добавления нового продукта
def add_product(products):
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").strip().lower() == 'да'

    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }
    products.append(new_product)


# Основная часть программы
file_path = 'products.json'  # Укажите путь к вашему JSON файлу

# Чтение текущих данных из файла
products = read_json(file_path)

# Добавление нового продукта
add_product(products)

# Запись обновленных данных обратно в файл
write_json(file_path, products)

# Вывод обновленного списка продуктов
print("Обновленный список продуктов:")
print_product_info(products)