import unittest
from requirements import check_minimum

class TestMinimum(unittest.TestCase):
    def test_min(self):
        self.assertTrue(check_minimum(600))

if __name__ == "__main__":
    unittest.main()
