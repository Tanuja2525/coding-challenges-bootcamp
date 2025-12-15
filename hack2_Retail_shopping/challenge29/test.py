import unittest
from tax_calculation import apply_tax

class TestTax(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(int(apply_tax(4000)), 4200)

if __name__ == "__main__":
    unittest.main()
