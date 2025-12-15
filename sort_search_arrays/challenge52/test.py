import unittest
from reverse_array import reverse_array

class TestReverseArray(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1])

    def test_single(self):
        self.assertEqual(reverse_array([5]), [5])

    def test_empty(self):
        self.assertEqual(reverse_array([]), [])


if __name__ == "__main__":
    unittest.main()
