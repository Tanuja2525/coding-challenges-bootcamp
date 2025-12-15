import unittest
from basic_item import item_total

class TestItemTotal(unittest.TestCase):
    def test_total(self):
        self.assertEqual(item_total(2, 100), 200)

if __name__ == "__main__":
    unittest.main()
