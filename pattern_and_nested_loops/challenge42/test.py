import unittest
from alternating_odd_series import alternating_series

class Test42(unittest.TestCase):
    def test_series(self):
        self.assertEqual(
            alternating_series(6),
            [1, -5, 9, -13, 17, -21]
        )

if __name__ == "__main__":
    unittest.main()
