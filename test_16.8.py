import unittest
from problem_16_8 import get_country_code

class CountryCodeTestCase(unittest.TestCase):
    """Tests for 'problem_16_8.py'"""
    def test_get_country_code(self):
        """Does 'Andorra' work?"""
        country_code = get_country_code('Andorra')
        self.assertEqual(country_code, 'ad')

unittest.main()
