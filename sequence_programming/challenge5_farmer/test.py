import unittest
from farmer import farmer_sales

class TestFarmerSales(unittest.TestCase):

    def test_sales_values(self):
        total, chemical_free = farmer_sales()
        self.assertGreater(total, 0)
        self.assertGreater(chemical_free, 0)

    def test_sales_relationship(self):
        total, chemical_free = farmer_sales()
        self.assertLessEqual(chemical_free, total)

    def test_return_type(self):
        total, chemical_free = farmer_sales()
        self.assertIsInstance(total, (int, float))
        self.assertIsInstance(chemical_free, (int, float))


if __name__ == "__main__":
    unittest.main()
