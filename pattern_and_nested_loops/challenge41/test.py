import unittest
from number_to_words import number_to_words

class Test41(unittest.TestCase):
    def test_number(self):
        self.assertEqual(
            number_to_words(270176),
            "Two Seven Zero One Seven Six"
        )

if __name__ == "__main__":
    unittest.main()
