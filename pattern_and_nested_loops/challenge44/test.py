import unittest
from reverse import reverse_number

class Test44(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_number(12345), 54321)

if __name__ == "__main__":
    unittest.main()
