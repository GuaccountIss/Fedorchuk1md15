import csv


csv_file = 'products.csv'

import csv


csv_file_path = 'products.csv'


products = []
total_sum = 0


with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product = row['Продукт']
        quantity = int(row['Количество'])
        price = int(row['Цена'])
        total_sum += quantity * price
        products.append((product, quantity, price))


print("Нужно купить:")
for product, quantity, price in products:
    print(f"{product} - {quantity} шт. за {price} руб.")

print(f"\nИтоговая сумма: {total_sum} руб.")