import unittest
from swap import swap_numbers

class TestSwapNumbers(unittest.TestCase):

    def test_normal_swap(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

    def test_same_numbers(self):
        self.assertEqual(swap_numbers(5, 5), (5, 5))

    def test_negative_numbers(self):
        self.assertEqual(swap_numbers(-1, -9), (-9, -1))

    def test_zero_case(self):
        self.assertEqual(swap_numbers(0, 10), (10, 0))


if __name__ == "__main__":
    unittest.main()
