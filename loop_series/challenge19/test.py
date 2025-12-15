import unittest
from squares_even_position import even_square_series

class TestEvenSquareSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(even_square_series(8), [4, 16, 36, 64])

    def test_small(self):
        self.assertEqual(even_square_series(2), [4])

    def test_odd_limit(self):
        self.assertEqual(even_square_series(7), [4, 16, 36])


if __name__ == "__main__":
    unittest.main()
