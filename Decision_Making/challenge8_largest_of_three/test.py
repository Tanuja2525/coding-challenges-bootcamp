import unittest
from largest import largest_of_three

class TestLargest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(largest_of_three(10, 20, 30), 30)

    def test_negative_values(self):
        self.assertEqual(largest_of_three(-10, -5, -1), -1)

    def test_equal_values(self):
        self.assertEqual(largest_of_three(5, 5, 5), 5)

    def test_mixed_values(self):
        self.assertEqual(largest_of_three(-1, 0, 1), 1)


if __name__ == "__main__":
    unittest.main()
