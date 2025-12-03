cities_info = {
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Home to the Eiffel Tower"
    },

    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "The most populated metropolitan area in the world"
    },

    "New York": {
        "country": "USA",
        "population": "8.3 million",
        "fact": "Known as the Big Apple"
    }
}

for cities, info in cities_info.items():
    if cities:
        print("\nCity:",cities)
        print('\tCountry',info['country'])
        print('\tPopulation',info['population'])
        print('\tFact',info['fact'])
