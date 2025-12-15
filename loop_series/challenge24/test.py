import unittest
from fibanocci_series import fibonacci_series

class TestFibonacciSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(fibonacci_series(8), [1, 1, 2, 3, 5, 8, 13, 21])

    def test_single(self):
        self.assertEqual(fibonacci_series(1), [1])

    def test_two(self):
        self.assertEqual(fibonacci_series(2), [1, 1])

    def test_zero(self):
        self.assertEqual(fibonacci_series(0), [])


if __name__ == "__main__":
    unittest.main()
