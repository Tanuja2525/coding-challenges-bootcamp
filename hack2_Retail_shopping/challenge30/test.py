import unittest
from promotional_discount import promo_discount

class TestPromo(unittest.TestCase):
    def test_promo(self):
        self.assertEqual(int(promo_discount("PROMO10", 1000)), 900)

if __name__ == "__main__":
    unittest.main()
