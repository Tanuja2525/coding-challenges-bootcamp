import unittest
from sum_average import sum_and_average

class TestSumAverage(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_and_average(10, 20), (30, 15))

    def test_negative_numbers(self):
        self.assertEqual(sum_and_average(-10, -20), (-30, -15))

    def test_mixed_numbers(self):
        self.assertEqual(sum_and_average(-5, 5), (0, 0))

    def test_zero_values(self):
        self.assertEqual(sum_and_average(0, 0), (0, 0))


if __name__ == "__main__":
    unittest.main()
