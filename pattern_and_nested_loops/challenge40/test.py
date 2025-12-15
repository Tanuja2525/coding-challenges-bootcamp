import unittest
from factorial import factorial_pattern

class TestPattern40(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            factorial_pattern(2),
            ["1", "2 6"]
        )

if __name__ == "__main__":
    unittest.main()
