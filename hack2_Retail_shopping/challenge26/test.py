import unittest
from iterative_item_entry import grand_total

class TestGrandTotal(unittest.TestCase):
    def test_grand(self):
        self.assertEqual(grand_total([100, 200, 300]), 600)

if __name__ == "__main__":
    unittest.main()
