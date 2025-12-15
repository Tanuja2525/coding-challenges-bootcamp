import unittest
from sum import sum_2d_array

class TestSum2DArray(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(sum_2d_array([[1,2],[3,4]]), 10)

    def test_empty(self):
        self.assertEqual(sum_2d_array([]), 0)


if __name__ == "__main__":
    unittest.main()
