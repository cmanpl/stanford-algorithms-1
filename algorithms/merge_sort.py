__author__ = 'cman'

"""
Merge Sort

- canonical divide and conquer introduction
- achieves O(nlgn) runtime
"""


def sort(lst):
    length = len(lst)
    if length >= 2:
        mid = length / 2
        left, right = lst[:mid], lst[mid:]
        sort(left)
        sort(right)
        l, r = 0, 0
        ll, lr = len(left), len(right)
        while l < ll and r < lr:
            if left[l] < right[r]:
                lst[l+r] = left[l]
                l += 1
            else:
                lst[l+r] = right[r]
                r += 1
        while l < ll:
            lst[l+r] = left[l]
            l += 1
        while r < lr:
            lst[l+r] = right[r]
            r += 1
    else:
        return lst
