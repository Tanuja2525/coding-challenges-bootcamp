import unittest
from store_to_array import create_array

class TestCreateArray(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(create_array([1, 2, 3]), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(create_array([]), [])

    def test_negative(self):
        self.assertEqual(create_array([-1, -5]), [-1, -5])


if __name__ == "__main__":
    unittest.main()
