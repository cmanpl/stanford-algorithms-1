__author__ = 'cman'


from assignments.one import assignment_one
import unittest
import itertools


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(AssignmentOneTest)


class AssignmentOneTest(unittest.TestCase):

    def test_reverse_list(self):
        reverse = [i for i in range(10)]
        reverse.reverse()
        expected = len(list(itertools.combinations(reverse, 2)))
        self.assertEqual(assignment_one.count_inversions(reverse), expected)

    def test_class_example(self):
        ex = [1, 3, 5, 2, 4, 6]
        expected = 3
        self.assertEqual(assignment_one.count_inversions(ex), expected)

    def test_no_inversions(self):
        data = range(10)
        expected = 0
        self.assertEqual(assignment_one.count_inversions(data), expected)


if __name__ == '__main__':
    unittest.main()
