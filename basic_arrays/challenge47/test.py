import unittest
from min_of_array import array_min

class TestArrayMin(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(array_min([3, 1, 2]), 1)

    def test_single(self):
        self.assertEqual(array_min([5]), 5)

    def test_empty(self):
        self.assertIsNone(array_min([]))


if __name__ == "__main__":
    unittest.main()
