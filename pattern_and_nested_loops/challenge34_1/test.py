import unittest
from  star_pattern import star_pattern

class TestPattern34(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            star_pattern(3),
            ["*****", "*****", "*****"]
        )

if __name__ == "__main__":
    unittest.main()
