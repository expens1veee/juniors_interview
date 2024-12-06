import unittest
from solution import appearance


class TestTimeFunctions(unittest.TestCase):

    def test_no_overlap(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594700000, 1594703600],
            'tutor': [1594720000, 1594723600]
        }
        result = appearance(intervals)
        self.assertEqual(result, 0, f"Expected 0, but got {result}")

    def test_full_overlap(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663200, 1594666800],
            'tutor': [1594663200, 1594666800]
        }
        result = appearance(intervals)
        self.assertEqual(result, 3600, f"Expected 3600, but got {result}")

    def test_empty_intervals(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [],  # Ученик (пустой)
            'tutor': [1594663290, 1594663430]
        }
        result = appearance(intervals)
        self.assertEqual(result, 0, f"Expected 0, but got {result}")


if __name__ == '__main__':
    unittest.main()