__author__ = 'cman'

from unittest import TestCase, TestLoader
from assignments.five import assignment_five
from assignments.five.assignment_five import INFINITY


def suite():
    return TestLoader().loadTestsFromTestCase(AssignmentFiveTest)


class AssignmentFiveTest(TestCase):

    def test_invalid_start(self):
        al = assignment_five.AdjacencyList()
        result = assignment_five.dijkstra(al, 1)
        self.assertEqual(result, {})

    def test_input_one(self):
        al = assignment_five.AdjacencyList('one.input')
        result = assignment_five.dijkstra(al, 1)
        self.assertEqual(result, {1: 0, 2: 1, 3: 5, 4: 6})

    def test_input_two(self):
        al = assignment_five.AdjacencyList('two.input')
        result = assignment_five.dijkstra(al, 1)
        self.assertEqual(result, {1: 0, 2: 5, 3: 5, 4: 10, 5: INFINITY, 6: INFINITY, 7: INFINITY, 8: INFINITY})

    def test_input_three(self):
        al = assignment_five.AdjacencyList('three.input')
        result = assignment_five.dijkstra(al, 1)
        self.assertEqual(result, {1: 0, 2: 1, 3: 2, 4: 3, 5: 4})
