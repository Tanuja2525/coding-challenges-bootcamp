import unittest
from odd_and_even_no import count_odd_even

class TestOddEven(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(count_odd_even([1, 2, 3, 4]), (2, 2))

    def test_all_even(self):
        self.assertEqual(count_odd_even([2, 4, 6]), (3, 0))

    def test_all_odd(self):
        self.assertEqual(count_odd_even([1, 3, 5]), (0, 3))

    def test_empty(self):
        self.assertEqual(count_odd_even([]), (0, 0))


if __name__ == "__main__":
    unittest.main()
