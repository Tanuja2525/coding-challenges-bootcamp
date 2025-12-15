import unittest
from search_key import search_element

class TestSearchElement(unittest.TestCase):

    def test_found(self):
        self.assertTrue(search_element([1, 2, 3], 2))

    def test_not_found(self):
        self.assertFalse(search_element([1, 2, 3], 5))

    def test_empty(self):
        self.assertFalse(search_element([], 1))


if __name__ == "__main__":
    unittest.main()
