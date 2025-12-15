import unittest
from series_1_to_N import natural_numbers

class TestNaturalNumbers(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(natural_numbers(5), [1, 2, 3, 4, 5])

    def test_single(self):
        self.assertEqual(natural_numbers(1), [1])

    def test_zero(self):
        self.assertEqual(natural_numbers(0), [])


if __name__ == "__main__":
    unittest.main()
