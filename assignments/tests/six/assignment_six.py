__author__ = 'cman'
import unittest
from assignments.six import q2

class Assignment6Q2(unittest.TestCase):

    def test_range(self):
        ints = [i for i in range(10)]
        meds = q2.medians(ints)
        self.assertEqual(meds, [0, 0, 1, 1, 2, 2, 3, 3, 4, 4])

    def test_reverse(self):
        ints = [i for i in reversed(range(10))]
        meds = q2.medians(ints)
        self.assertEqual(meds, [9, 8, 8, 7, 7, 6, 6, 5, 5, 4])

