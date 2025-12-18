class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title(), "is a 3-star restaurant.\n" \
        "It is located in New York.")

    def open_restaurant(self):
        print(self.name.title(), "is open now!")


restaurant = Restaurant('The Shine','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
