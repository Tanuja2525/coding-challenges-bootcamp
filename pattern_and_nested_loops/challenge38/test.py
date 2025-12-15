import unittest
from fibanocci_series import fibonacci_pattern

class TestPattern38(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            fibonacci_pattern(3),
            ["1", "1 2", "3 5 8"]
        )

if __name__ == "__main__":
    unittest.main()
