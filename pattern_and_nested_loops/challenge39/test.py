import unittest
from perfect_squares_alternate_sign import square_sign_pattern

class TestPattern39(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            square_sign_pattern(1),
            ["1 -4 9 -16 25 -36"]
        )

if __name__ == "__main__":
    unittest.main()
