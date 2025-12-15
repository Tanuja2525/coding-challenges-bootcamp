import unittest
from loyalty_points import loyalty_points

class TestLoyalty(unittest.TestCase):
    def test_points(self):
        self.assertEqual(loyalty_points(1250), 12)

if __name__ == "__main__":
    unittest.main()
