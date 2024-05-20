import csv

# Функция для чтения данных из CSV файла
def read_csv(file_path):
    products = []
    with open(file_path, 'F:\Admin\Desktop\products.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # Пропускаем заголовок
        next(reader)
        for row in reader:
            product = {
                'name': row[0],
                'quantity': int(row[1]),
                'price': int(row[2])
            }
            products.append(product)
    return products

# Функция для подсчета итоговой суммы и вывода данных
def print_purchase_list(products):
    total_sum = 0
    print("Нужно купить:")
    for product in products:
        total_sum += product['quantity'] * product['price']
        print(f"{product['name']} - {product['quantity']} шт. за {product['price']} руб.")
    print(f"Итоговая сумма: {total_sum} руб.")

# Основная часть программы
file_path = 'F:\Admin\Desktop'  # Укажите путь к вашему CSV файлу
products = read_csv(file_path)
print_purchase_list(products)
