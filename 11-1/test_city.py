import unittest

from city_func  import city_functions

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		res = city_functions('wuhan', 'China')
		self.assertEqual(res, 'wuhan, China')
	
	def test_city_country_population(self):
		res = city_functions('shanghai', 'China', '30Million')
		self.assertEqual(res, 'shanghai, China - population 30Million')

unittest.main()
