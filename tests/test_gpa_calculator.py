import unittest

from gpa_calculator import calculate_gpa, calculate_cgpa


class TestGpaCalculator(unittest.TestCase):

    def test_calculate_gpa(self):
        courses = [
            (4.0, 3),
            (3.0, 3),
            (3.5, 2),
        ]

        self.assertAlmostEqual(calculate_gpa(courses), 3.5)

    def test_gpa_without_courses(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])

    def test_gpa_invalid_grade_points(self):
        with self.assertRaises(ValueError):
            calculate_gpa([(4.5, 3)])

    def test_gpa_invalid_credit_hours(self):
        with self.assertRaises(ValueError):
            calculate_gpa([(3.5, 0)])

    def test_calculate_cgpa(self):
        semesters = [
            (3.5, 15),
            (3.8, 18),
        ]

        self.assertAlmostEqual(
            calculate_cgpa(semesters),
            3.6636363636,
        )

    def test_cgpa_without_semesters(self):
        with self.assertRaises(ValueError):
            calculate_cgpa([])

    def test_cgpa_invalid_semester_gpa(self):
        with self.assertRaises(ValueError):
            calculate_cgpa([(4.5, 15)])

    def test_cgpa_invalid_credit_hours(self):
        with self.assertRaises(ValueError):
            calculate_cgpa([(3.5, 0)])


if __name__ == "__main__":
    unittest.main()
