import unittest
from create_array import display_2d_array

class TestDisplay2DArray(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(display_2d_array([[1,2],[3,4]]), [[1,2],[3,4]])

    def test_empty(self):
        self.assertEqual(display_2d_array([]), [])


if __name__ == "__main__":
    unittest.main()
