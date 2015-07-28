__author__ = 'cman'

import unittest
from assignments.six import assignment_six
import random


class AssignmentSixTest(unittest.TestCase):

    def test_rank(self):
        test = [i for i in range(0, 10, 2)]
        self.assertEqual(assignment_six.rank(test, -1), -1)
        self.assertEqual(assignment_six.rank(test, 0), 0)
        self.assertEqual(assignment_six.rank(test, 1), 0)
        self.assertEqual(assignment_six.rank(test, 6), 3)
        self.assertEqual(assignment_six.rank(test, 7), 3)
        self.assertEqual(assignment_six.rank(test, 8), 4)
        self.assertEqual(assignment_six.rank(test, 9), 4)
