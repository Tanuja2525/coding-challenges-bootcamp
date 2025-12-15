import unittest
from even_or_odd import even_or_odd

class TestEvenOdd(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(0), "Even")

    def test_odd_numbers(self):
        self.assertEqual(even_or_odd(3), "Odd")
        self.assertEqual(even_or_odd(-5), "Odd")


if __name__ == "__main__":
    unittest.main()
