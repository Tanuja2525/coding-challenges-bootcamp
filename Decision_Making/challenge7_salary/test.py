import unittest
from salary_tax import tax_check

class TestTaxCheck(unittest.TestCase):

    def test_above_limit(self):
        self.assertEqual(tax_check("A", 400000), "A must pay tax")

    def test_equal_limit(self):
        self.assertEqual(tax_check("B", 300000), "B does not need to pay tax")

    def test_below_limit(self):
        self.assertEqual(tax_check("C", 150000), "C does not need to pay tax")


if __name__ == "__main__":
    unittest.main()
