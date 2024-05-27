import json



def add_product(products):
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").strip().lower() == 'да'

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    products.append(new_product)



def print_products(products):
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = "В наличии" if product['available'] else "Нет в наличии!"

        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(f"{available}\n")



file_path = 'products.json'


try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {'products': []}


add_more = input("Хотите добавить новый продукт? (да/нет): ").strip().lower() == 'да'

while add_more:
    add_product(data['products'])
    add_more = input("Хотите добавить еще один продукт? (да/нет): ").strip().lower() == 'да'


with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


print("\nИтоговый список продуктов:")
print_products(data['products'])