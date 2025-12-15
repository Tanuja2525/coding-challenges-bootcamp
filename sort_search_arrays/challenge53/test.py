import unittest
from sort_array import sort_array

class TestSortArray(unittest.TestCase):

    def test_ascending(self):
        self.assertEqual(sort_array([3, 1, 2], "asc"), [1, 2, 3])

    def test_descending(self):
        self.assertEqual(sort_array([3, 1, 2], "desc"), [3, 2, 1])

    def test_single(self):
        self.assertEqual(sort_array([5], "asc"), [5])

    def test_empty(self):
        self.assertEqual(sort_array([], "asc"), [])


if __name__ == "__main__":
    unittest.main()
