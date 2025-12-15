import unittest
from series_of_odd import odd_numbers

class TestOddNumbers(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(odd_numbers(10), [1, 3, 5, 7, 9])

    def test_small(self):
        self.assertEqual(odd_numbers(1), [1])

    def test_zero(self):
        self.assertEqual(odd_numbers(0), [])


if __name__ == "__main__":
    unittest.main()
