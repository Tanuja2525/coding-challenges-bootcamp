import unittest
from multiply import multiply_matrices

class TestMatrixMultiplication(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(
            multiply_matrices([[1,2],[3,4]], [[5,6],[7,8]]),
            [[19,22],[43,50]]
        )


if __name__ == "__main__":
    unittest.main()
