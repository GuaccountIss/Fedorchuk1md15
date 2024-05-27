class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

newRestaurant = Restaurant("Гурман", "Французская кухня")

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


restaurant1 = Restaurant("Гурман", "Французская кухня")
restaurant2 = Restaurant("Суши-бар", "Японская кухня")
restaurant3 = Restaurant("Пицца Хаус", "Итальянская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

restaurant1 = Restaurant("Гурман", "Французская кухня", 4.5)
restaurant2 = Restaurant("Восточный уголок", "Китайская кухня", 4.0)
restaurant3 = Restaurant("Пицца Палаццо", "Итальянская кухня", 4.8)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(4.7)
restaurant1.describe_restaurant()