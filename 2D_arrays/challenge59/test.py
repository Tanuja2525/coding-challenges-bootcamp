import unittest
from transpose import transpose_matrix

class TestTransposeMatrix(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(
            transpose_matrix([[1,2,3],[4,5,6]]),
            [[1,4],[2,5],[3,6]]
        )

    def test_single(self):
        self.assertEqual(transpose_matrix([[1]]), [[1]])


if __name__ == "__main__":
    unittest.main()
