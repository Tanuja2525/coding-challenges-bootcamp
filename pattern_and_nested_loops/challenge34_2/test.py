import unittest
from number_block import number_pattern_fixed

class TestNumberPattern34(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(
            number_pattern_fixed(4),
            ["12345", "12345", "12345", "12345"]
        )

    def test_single_row(self):
        self.assertEqual(
            number_pattern_fixed(1),
            ["12345"]
        )

    def test_zero_rows(self):
        self.assertEqual(
            number_pattern_fixed(0),
            []
        )


if __name__ == "__main__":
    unittest.main()
