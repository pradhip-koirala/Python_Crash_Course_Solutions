def city_country(city, country, population = ''):
    c_c = city+ ", " + country 
    formatted_detail = c_c.title() + ' - ' + "population " + str(population)

    return formatted_detail

# print(city_country('taunggyi', 'myanamar', 50))
