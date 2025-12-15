import unittest
from simpleinterest import simple_interest

class TestSimpleInterest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(simple_interest(1000, 10, 2), 200)

    def test_zero_principal(self):
        self.assertEqual(simple_interest(0, 10, 2), 0)

    def test_zero_rate(self):
        self.assertEqual(simple_interest(1000, 0, 2), 0)

    def test_zero_time(self):
        self.assertEqual(simple_interest(1000, 10, 0), 0)


if __name__ == "__main__":
    unittest.main()
