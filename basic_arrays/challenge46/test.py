import unittest
from sum_of_array import array_sum

class TestArraySum(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(array_sum([1, 2, 3]), 6)

    def test_empty(self):
        self.assertEqual(array_sum([]), 0)

    def test_negative(self):
        self.assertEqual(array_sum([-1, -2, 3]), 0)


if __name__ == "__main__":
    unittest.main()
