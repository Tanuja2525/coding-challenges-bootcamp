import unittest
from check_element import search_2d_array

class TestSearch2DArray(unittest.TestCase):

    def test_found(self):
        self.assertTrue(search_2d_array([[1,2],[3,4]], 3))

    def test_not_found(self):
        self.assertFalse(search_2d_array([[1,2],[3,4]], 5))

    def test_empty(self):
        self.assertFalse(search_2d_array([], 1))


if __name__ == "__main__":
    unittest.main()
