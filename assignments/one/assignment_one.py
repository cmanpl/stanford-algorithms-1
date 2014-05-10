#!/bin/env python
__author__ = 'cman'

"""
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
entry of an array. Because of the large size of this array, you should implement the fast divide-and-conquer algorithm
covered in the video lectures.
"""


from utils import data


def count_inversions(ints):
    return _sort_and_count(ints)[1]


def _sort_and_count(ints):
    size = len(ints)
    if size <= 1:
        return ints, 0
    else:
        result = []
        mid = size / 2
        left, count_left = _sort_and_count(ints[:mid])
        right, count_right = _sort_and_count(ints[mid:])
        length_left, length_right = len(left), len(right)
        l, r = 0, 0
        count = 0
        while l < length_left and r < length_right:
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
                count += length_left - l
        while l < length_left:
            result.append(left[l])
            l += 1
        while r < length_right:
            result.append(right[r])
            r += 1
        return result, count + count_left + count_right


if __name__ == '__main__':
    ints = data.read_ints('assignment_one.input')
    print count_inversions(ints)