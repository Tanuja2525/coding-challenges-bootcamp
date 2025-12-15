import unittest
from number_increasing_custom2 import number_sequence_pattern

class TestPattern37(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            number_sequence_pattern(4),
            ["1", "12", "123", "1234"]
        )

if __name__ == "__main__":
    unittest.main()
