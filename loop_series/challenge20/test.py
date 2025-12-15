import unittest
from custom_series import increasing_diff_series

class TestIncreasingDiffSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(increasing_diff_series(6), [1, 2, 4, 7, 11, 16])

    def test_single(self):
        self.assertEqual(increasing_diff_series(1), [1])

    def test_zero(self):
        self.assertEqual(increasing_diff_series(0), [])


if __name__ == "__main__":
    unittest.main()
