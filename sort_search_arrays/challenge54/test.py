import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 4), 3)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3], 6), -1)

    def test_single(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_empty(self):
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
