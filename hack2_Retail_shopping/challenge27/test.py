import unittest
from discount_apply import apply_discounts

class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(int(apply_discounts(11000, 25)), 9405)

if __name__ == "__main__":
    unittest.main()
