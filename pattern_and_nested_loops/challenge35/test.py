import unittest
from star_increasing import increasing_star

class TestPattern35(unittest.TestCase):
    def test_pattern(self):
        self.assertEqual(
            increasing_star(4),
            ["*", "**", "***", "****"]
        )

if __name__ == "__main__":
    unittest.main()
