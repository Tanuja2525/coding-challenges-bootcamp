import unittest
from max_of_array import array_max

class TestArrayMax(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(array_max([3, 7, 2]), 7)

    def test_single(self):
        self.assertEqual(array_max([5]), 5)

    def test_empty(self):
        self.assertIsNone(array_max([]))


if __name__ == "__main__":
    unittest.main()
