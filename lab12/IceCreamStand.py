class IceCreamStand:
    def init(self, restaurant_name, cuisine_type, rating=0, flavors=None, location="", hours=""):
        if flavors is None:
            flavors = []
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.flavors = flavors
        self.location = location
        self.hours = hours

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            return f"Сорт {flavor} добавлен."
        else:
            return f"Сорт {flavor} уже есть в списке."

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return f"Сорт {flavor} удален."
        else:
            return f"Сорта {flavor} нет в списке."

    def show_flavors(self):
        return "\n".join(self.flavors)

    def describe_restaurant(self):
        return (f"Название ресторана: {self.restaurant_name}\n"
                f"Тип кухни: {self.cuisine_type}\n"
                f"Рейтинг: {self.rating}\n"
                f"Локация: {self.location}\n"
                f"Время работы: {self.hours}")