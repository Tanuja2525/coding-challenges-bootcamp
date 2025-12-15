import unittest
from custom2_series import custom_series

class TestCustomSeries(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(custom_series(5), [1, 2, 6, 15, 31])

    def test_single(self):
        self.assertEqual(custom_series(1), [1])

    def test_two(self):
        self.assertEqual(custom_series(2), [1, 2])


if __name__ == "__main__":
    unittest.main()
