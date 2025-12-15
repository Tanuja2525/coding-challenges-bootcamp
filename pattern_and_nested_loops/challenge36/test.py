import unittest
from number_increasing import number_repeat_pattern

class TestPattern36(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            number_repeat_pattern(4),
            ["1", "22", "333", "4444"]
        )

if __name__ == "__main__":
    unittest.main()
