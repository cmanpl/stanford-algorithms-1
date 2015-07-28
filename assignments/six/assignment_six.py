__author__ = 'cman'
from utils import data


def first_solution(ints):
    targets = {i: False for i in range(-10000, 10001)}
    targets_hit = 0
    lookup = {}
    for x in ints:
        # O(n)
        if x not in lookup:
            # O(1)
            lookup[x] = True
            for t in targets.keys():
                # O(t)
                # y = t - x
                if (t - x) in lookup:
                    # O(1)
                    targets_hit += 1
                    del targets[t]
    return targets_hit


def second_solution(ints):
    lookup = {i: True for i in ints}
    sorted_ints = sorted([i for i in lookup.keys()])
    size = len(sorted_ints)
    targets = {}
    for i in sorted_ints:
        # y = t - x
        mn = -10000 - i
        mx = 10000 - i
        r = rank(sorted_ints, mn)
        if r < 0:
            r = 0
        while r < size and sorted_ints[r] <= mx:
            t = i + sorted_ints[r]
            if t >= -10000:
                targets[t] = None
            r += 1
    return len(targets)


def third_solution(ints):
    lookup = {i: True for i in ints}
    sorted_ints = sorted([i for i in lookup.keys()])
    size = len(sorted_ints)
    targets = {}
    for i in sorted_ints:
        r = rank(sorted_ints, -i)
        if r < 0:
            r = 0
        j = r
        while j < size:
            val = sorted_ints[j] + i
            if val >= -10000 and val <= 10000:
                targets[val] = None
            else:
                break
            j += 1
        j = r
        while j >= 0:
            val = sorted_ints[j] + i
            if val >= -10000 and val <= 10000:
                targets[val] = None
            else:
                break
            j -= 1
    return len(targets)


def rank(sorted_list, item):
    mn, mx = 0, len(sorted_list) - 1
    mid = 0
    while mn <= mx:
        mid = mn + (mx - mn) / 2
        mid_value = sorted_list[mid]
        if mid_value == item:
            return mid
        elif mid_value < item:
            mn = mid + 1
        else:
            mx = mid - 1
    return mid - 1 if sorted_list[mid] > item else mid


if __name__ == '__main__':
    # x + y = t for t in range (-10000, 10000) inclusive
    ints = data.read_ints('assignment_six.input')
    result = second_solution(ints)
    print(result)

