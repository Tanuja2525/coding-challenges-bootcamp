import unittest
from student import student_result

class TestStudentResult(unittest.TestCase):

    def test_first_class(self):
        self.assertEqual(student_result("A", 70, 80, 90)[2], "1st Class")

    def test_second_class(self):
        self.assertEqual(student_result("B", 55, 50, 52)[2], "2nd Class")

    def test_pass_class(self):
        self.assertEqual(student_result("C", 40, 35, 38)[2], "Pass Class")

    def test_fail(self):
        self.assertEqual(student_result("D", 20, 30, 10)[2], "Fail")


if __name__ == "__main__":
    unittest.main()
