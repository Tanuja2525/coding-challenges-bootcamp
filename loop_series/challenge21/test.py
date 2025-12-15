import unittest
from square_series import square_series

class TestSquareSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(square_series(5), [1, 4, 9, 16, 25])

    def test_single(self):
        self.assertEqual(square_series(1), [1])

    def test_zero(self):
        self.assertEqual(square_series(0), [])


if __name__ == "__main__":
    unittest.main()
