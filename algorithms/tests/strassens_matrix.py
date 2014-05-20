__author__ = 'cman'
import unittest
from algorithms import strassens_matrix
from utils import data
import copy


class StrassenMatrixTest(unittest.TestCase):

    def test_odd_matrix_mult(self):
        sizes = [2, 9, 10, 2**4]
        for size in sizes:
            a = [[1 for i in range(size)] for j in range(size)]
            b = [[1 for i in range(size)] for j in range(size)]
            expected = [[size for i in range(size)] for j in range(size)]
            result = strassens_matrix.multipy(a, b)
            self.assertEqual(result, expected)

    def test_identity_matrix_mult(self):
        size = 10
        a = data.random_matrix(size)
        identity = data.build_identity_matrix(size)
        expected = copy.deepcopy(a)
        self.assertEqual(strassens_matrix.multipy(a, identity), expected)

    def test_quadrant_split(self):
        start = [
            [1, 2],
            [3, 4]
        ]
        result = strassens_matrix.split_quadrants(start)
        for i, r in enumerate(result):
            self.assertEqual(r, [[i+1]])

    def test_add(self):
        size = 10
        a, b = [[[1 for i in range(size)] for j in range(size)] for k in range(2)]
        expected = [[2 for i in range(size)] for j in range(size)]
        result = strassens_matrix.add(a, b)
        self.assertEqual(result, expected)

    def test_sub(self):
        size = 10
        a, b = [[[1 for i in range(size)] for j in range(size)] for k in range(2)]
        expected = [[0 for i in range(size)] for j in range(size)]
        result = strassens_matrix.subtract(a, b)
        self.assertEqual(result, expected)
