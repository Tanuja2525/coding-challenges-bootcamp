import unittest
from number_repeat import number_pattern_same

class TestPattern33(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            number_pattern_same(3),
            ["11111", "22222", "33333"]
        )

if __name__ == "__main__":
    unittest.main()
