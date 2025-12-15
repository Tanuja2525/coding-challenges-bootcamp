import unittest
from membership_discount import membership_discount

class TestMembership(unittest.TestCase):
    def test_member(self):
        self.assertEqual(int(membership_discount(1000, 'y')), 980)

if __name__ == "__main__":
    unittest.main()
