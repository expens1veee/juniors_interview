import unittest
from juniors_interview3.task1 import solution


class TestTasks(unittest.TestCase):
    def testsum(self):
        self.assertEqual(solution.sum_two(1, 2), 3)

    def testsum2(self):
        with self.assertRaises(TypeError):
            solution.sum_two(2, 2.7)


if __name__ == '__main__':
    unittest.main()