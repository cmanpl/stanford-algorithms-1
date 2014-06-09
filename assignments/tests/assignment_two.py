__author__ = 'cman'
import unittest
from assignments import two
from assignments.two import assignment_two
from utils import data

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(AssignmentTwoTest)


class AssignmentTwoTest(unittest.TestCase):

    def test_reverse_lst(self):
        lst = [i for i in reversed(range(1, 100))]
        assignment_two.quick_sort(lst)
        self.assertEqual(lst, sorted(lst))

    def test_random_lst(self):
        lst = data.random_ints(100, 1, 100)
        assignment_two.quick_sort(lst)
        self.assertEqual(lst, sorted(lst))

    def test_assignment_two_input(self):
        pivotfns = [
            assignment_two.random_pivot, assignment_two.first_elem_pivot, assignment_two.last_elem_pivot, assignment_two.median_3_pivot
        ]
        for pivotfn in pivotfns:
            lst = data.read_ints('assignment_two.input')
            comparisons = assignment_two.quick_sort(lst, pivotfn)
            self.assertEqual(lst, sorted(lst))
            print((pivotfn.__name__, comparisons))
