import unittest
from discount import calculate_discount

class TestDiscount(unittest.TestCase):

    def test_normal_discount(self):
        self.assertEqual(calculate_discount(1000, 10), 900)

    def test_zero_discount(self):
        self.assertEqual(calculate_discount(1000, 0), 1000)

    def test_full_discount(self):
        self.assertEqual(calculate_discount(1000, 100), 0)

    def test_decimal_amount(self):
        self.assertAlmostEqual(calculate_discount(500.5, 10), 450.45)


if __name__ == "__main__":
    unittest.main()
