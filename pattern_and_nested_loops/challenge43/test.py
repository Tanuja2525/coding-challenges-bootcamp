import unittest
from separation_of_whole_fraction import separate_whole_fraction

class Test43(unittest.TestCase):
    def test_value(self):
        self.assertEqual(separate_whole_fraction(12.75), (12, 0.75))

if __name__ == "__main__":
    unittest.main()
