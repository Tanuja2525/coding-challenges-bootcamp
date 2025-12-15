import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):

    def test_leap_years(self):
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2000))

    def test_non_leap_years(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2023))


if __name__ == "__main__":
    unittest.main()
