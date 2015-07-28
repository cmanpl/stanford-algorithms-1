__author__ = 'cman'
from utils import data
import heapq


def _rebalance(minheap, maxheap):
    minlen = len(minheap)
    maxlen = len(maxheap)
    if minlen > maxlen:
        if (minlen - maxlen) > 1:
            minval = heapq.heappop(minheap)
            heapq.heappush(maxheap, -minval)
    else:
        if (maxlen - minlen) > 1:
            maxval = -heapq.heappop(maxheap)
            heapq.heappush(minheap, maxval)


def medians(ints):
    minheap, maxheap = [], []
    if len(ints) < 2:
        raise Exception('median maintenance algo only relevant for >= 2 elements')
    a = ints.pop(0)
    meds = [a]
    b = ints.pop(0)
    # add smaller to the max heap, bigger to min heap
    if a > b:
        meds.append(b)
        heapq.heappush(minheap, a)
        heapq.heappush(maxheap, -b)
    else:
        meds.append(a)
        heapq.heappush(minheap, b)
        heapq.heappush(maxheap, -a)
    for i in ints:
        if i < -maxheap[0]:
            heapq.heappush(maxheap, -i)
        else:
            heapq.heappush(minheap, i)
        _rebalance(minheap, maxheap)
        if len(minheap) > len(maxheap):
            med = minheap[0]
        elif len(maxheap) > len(minheap):
            med = -maxheap[0]
        else:
            med = min(-maxheap[0], minheap[0])
        meds.append(med)
    return meds

if __name__ == '__main__':
    ints = data.read_ints('q2.input')
    meds = medians(ints)
    sum = 0
    for m in meds:
        sum = (sum + m) % 10000
    print(sum)

