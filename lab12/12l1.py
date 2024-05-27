class Restaurant:
    def init(self, restaurant_name, cuisine_type, rating=0):
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

class IceCreamStand(Restaurant):
    def init(self, restaurant_name, cuisine_type, rating=0, flavors=None):
        super().init(restaurant_name, cuisine_type, rating)
        if flavors is None:
            flavors = []
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого в наличии:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Ледяная радость", "Кафе-мороженое", 4.5, ["Ванильное", "Шоколадное", "Клубничное", "Мятное"])


ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.show_flavors()