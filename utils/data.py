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
