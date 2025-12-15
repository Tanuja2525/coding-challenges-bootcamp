import unittest
from payment_rules import payment_total

class TestPayment(unittest.TestCase):
    def test_card(self):
        self.assertEqual(int(payment_total(1000, "card")), 1020)

if __name__ == "__main__":
    unittest.main()
