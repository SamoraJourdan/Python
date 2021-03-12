import unittest
from tiy291 import citify

class TestCountryCity(unittest.TestCase):

	def test_city_country(self):
		cc = citify('joburg', 'south africa')
		self.assertEqual(cc, 'Joburg, South Africa')

	def test_city_country_pop(self):
		cc = citify('joburg', 'south africa', 500000)
		self.assertEqual(cc, 'Joburg, South Africa - Population 500000')	

if __name__ == '__main__':
	unittest.main()