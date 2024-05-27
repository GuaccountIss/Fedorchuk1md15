import json


file_path = 'products.json'


with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


for product in data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = "В наличии" if product['available'] else "Нет в наличии!"

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(f"{available}\n")