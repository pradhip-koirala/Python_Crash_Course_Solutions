def make_car (manufacturer, model,**detail):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in detail.items():
        car[key] = value
    return car

car = make_car('subaru','outback',
                  color ='blue',
                  tow_package =True)

print(car)

toyota = make_car('toyota','suiz',
                  color='red',
                  seat = 4)

print(toyota)