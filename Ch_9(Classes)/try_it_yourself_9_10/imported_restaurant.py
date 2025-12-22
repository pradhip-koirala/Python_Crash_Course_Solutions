from restaurant import Restaurant


restaurant = Restaurant('The Shine','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# print("NO. of customer served:",restaurant.number_served)
restaurant.number_served =24
restaurant.customer_served()

restaurant.increment_number_served(76)
restaurant.customer_served()