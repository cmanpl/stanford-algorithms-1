__author__ = 'cman'
from random import randint


def quick_sort(data, pivotfn=None):
    if pivotfn is None:
        pivotfn = random_pivot
    return _sort(data, 0, len(data) - 1, pivotfn)


def _sort(data, start, end, pivotfn):
    """
    Sort the data between the start and end indices.

    Since end is the index of the final element, the sorted subsection has length
    (end - start + 1).
    """
    # each recursive all contributes len - 1 comparisons. len - 1 = end - start - 1 + 1 = end - start
    if end - start == 1:
        if data[start] > data[end]:
            _swap(data, start, end)
        return 1
    elif end - start > 1:
        comps = end - start
        partition = _partition(data, start, end, pivotfn)
        comps += _sort(data, start, partition - 1, pivotfn)
        comps += _sort(data, partition + 1, end, pivotfn)
        return comps
    else:
        return 0


def _partition(data, start, end, pivotfn):
    p = pivotfn(data, start, end)
    pivot = data[p]
    _swap(data, p, start)
    p = start + 1
    for i, d in enumerate(data[start + 1:]):
        if d < pivot:
            _swap(data, p, i + start + 1)
            p += 1
    _swap(data, start, p - 1)
    return p - 1


def _swap(data, start, end):
    temp = data[start]
    data[start] = data[end]
    data[end] = temp


def random_pivot(data, start, end):
    # random pivot between start and end inclusive
    return randint(start, end)


def first_elem_pivot(data, start, end):
    return start


def last_elem_pivot(data, start, end):
    return end


def median_3_pivot(data, start, end):
    mid = (end - start) / 2 + start
    ds, dm, de = data[start], data[mid], data[end]
    if ds < dm:
        # [ds, dm]
        if ds > de:
            return start
        elif dm < de:
            return mid
        else:
            return end
    else:
        # [dm, ds]
        if ds < de:
            return start
        elif de < dm:
            return mid
        else:
            return end


if __name__ == '__main__':
    s = [i for i in reversed(range(10))]
    quick_sort(s, median_3_pivot)
    print(s)
