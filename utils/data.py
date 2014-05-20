__author__ = 'cman'

"""
Functions that assist in generating data.
"""

import random


def random_ints(size, range_start=0, range_end=100):
    result = []
    for i in range(size):
        result.append(random.randint(range_start, range_end))
    return result


def read_ints(file_name):
    result = []
    with open(file_name) as ints:
        for line in ints:
            result.append(int(line.strip()))
    return result


def build_identity_matrix(size):
    result = []
    for j in range(size):
        result.append([1 if i == j else 0 for i in range(size)])
    return result


def random_matrix(size, range_start=0, range_end=100):
    result = []
    for j in range(size):
        result.append([random.randint(range_start, range_end) for i in range(size)])
    return result
