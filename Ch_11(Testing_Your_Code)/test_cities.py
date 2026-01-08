import unittest
from city_country import c_c
from population import city_country


class TestCityCountry(unittest.TestCase):
    
    def test_city_country_basic(self):
        country_city = c_c("yangoon", 'myanmar')
        self.assertEqual(country_city, 'Yangoon, Myanmar')

    def test_city_country(self):
        country_city = city_country('yangoon', 'myanmar', population='50 million')
        self.assertEqual(country_city, 'Yangoon, Myanmar - population 50 million')

unittest.main()