import unittest
from custom3_series import mixed_increment_series

class TestMixedIncrementSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(
            mixed_increment_series(9),
            [1, 5, 13, 17, 25, 29, 37, 41, 49]
        )

    def test_single(self):
        self.assertEqual(mixed_increment_series(1), [1])

    def test_two(self):
        self.assertEqual(mixed_increment_series(2), [1, 5])


if __name__ == "__main__":
    unittest.main()
