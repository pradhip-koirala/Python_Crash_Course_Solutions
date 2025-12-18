class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.name.title(), "is a 3-star restaurant.\n" \
        "It is located in New York.")

    def open_restaurant(self):
        print(self.name.title(), "is open now!")

    def customer_served(self):
        print("No. of customer served: "+str(self.number_served))
    
    def increment_number_served(self, total_customer):
        self.number_served += total_customer



restaurant = Restaurant('The Shine','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# print("NO. of customer served:",restaurant.number_served)
restaurant.number_served =24
restaurant.customer_served()

restaurant.increment_number_served(76)
restaurant.customer_served()