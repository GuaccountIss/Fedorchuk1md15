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
    def init(self, restaurant_name, cuisine_type, rating=0, flavors=None, location="", hours=""):
        super().init(restaurant_name, cuisine_type, rating)
        if flavors is None:
            flavors = []
        self.flavors = flavors
        self.location = location
        self.hours = hours
        self.stick_ice_creams = []
        self.soft_ice_creams = []

    def describe_location_and_hours(self):
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.hours}")

    def show_flavors(self):
        print("Сорта мороженого в наличии:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт {flavor} добавлен.")
        else:
            print(f"Сорт {flavor} уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт {flavor} удален.")
        else:
            print(f"Сорта {flavor} нет в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт {flavor} есть в наличии.")
        else:
            print(f"Сорта {flavor} нет в наличии.")

    def add_stick_ice_cream(self, flavor):
        if flavor not in self.stick_ice_creams:
            self.stick_ice_creams.append(flavor)
            print(f"Мороженое на палочке {flavor} добавлено.")
        else:
            print(f"Мороженое на палочке {flavor} уже есть в списке.")

    def show_stick_ice_creams(self):
        print("Мороженое на палочке в наличии:")
        for flavor in self.stick_ice_creams:
            print(f"- {flavor}")

    def add_soft_ice_cream(self, flavor):
        if flavor not in self.soft_ice_creams:
            self.soft_ice_creams.append(flavor)
            print(f"Мягкое мороженое {flavor} добавлено.")
        else:
            print(f"Мягкое мороженое {flavor} уже есть в списке.")

    def show_soft_ice_creams(self):
        print("Мягкое мороженое в наличии:")
        for flavor in self.soft_ice_creams:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Ледяная радость", "Кафе-мороженое", 4.5, ["Ванильное", "Шоколадное"], "Центр города", "10:00 - 22:00")


ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.describe_location_and_hours()
ice_cream_stand.show_flavors()

ice_cream_stand.add_flavor("Клубничное")
ice_cream_stand.remove_flavor("Ванильное")
ice_cream_stand.check_flavor("Шоколадное")

ice_cream_stand.add_stick_ice_cream("Шоколадное на палочке")
ice_cream_stand.show_stick_ice_creams()

ice_cream_stand.add_soft_ice_cream("Мягкое ванильное")
ice_cream_stand.show_soft_ice_creams()