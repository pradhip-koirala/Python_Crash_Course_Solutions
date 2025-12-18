class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("\n"+self.name.title(), "is a 3-star restaurant.\n" \
        "It is located in New York.")

    def open_restaurant(self):
        print(self.name.title(), "is open now!")

#first restaurant
restaurant = Restaurant('The Shine','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#second restaurant
sec_res = Restaurant('Amul','indian')
sec_res.describe_restaurant()
sec_res.open_restaurant()

#third restaurant
third_res = Restaurant('the bangkok','thai')
third_res.describe_restaurant()
third_res.open_restaurant()
