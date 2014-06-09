import copy
import random
import sys

__author__ = 'cman'


def read_adjacency_list(file_name):
    result = {}
    for line in open(file_name):
        numbers = [int(i.strip()) for i in line.split()]
        result[numbers[0]] = numbers[1:]
    return result


def _sort(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def compute_min_cut(adjacency_list):
    al = {k: set(v) for k, v in adjacency_list.items()}
    counts = {}
    # Counting assumes there is 0 or 1 paths between adjacent nodes
    for head, tails in adjacency_list.items():
        for tail in tails:
            key = _sort(head, tail)
            counts[key] = 1
    while len(al) > 2:
        tail, = random.sample(al.keys(), 1)
        head, = random.sample(al[tail], 1)
        updates = []
        for edge, count in counts.items():
            t, h = edge
            if h == head:
                updates.append((edge, _sort(tail, t), count))
            elif t == head:
                updates.append((edge, _sort(tail, h), count))
        for old, new, count in updates:
            del counts[old]
            if new[0] == new[1]:
                if new in counts:
                    del counts[new]
                continue
            c = counts.get(new, 0)
            c += count
            counts[new] = c
        al[tail].update(al[head])
        del al[head]
        for v, e in al.items():
            if head in e:
                e.remove(head)
                e.add(tail)
        if tail in al[tail]:
            al[tail].remove(tail)
    h, t = al.keys()
    h, t = _sort(h, t)
    return h, t, counts[(h, t)]


def p(d):
    for k in sorted(d.keys()):
        print(k, '->', d[k])

if __name__ == '__main__':
    al = read_adjacency_list('assignment_three.input')
    trials = len(al) ** 2
    print('Running', trials, 'trials')
    ten_percent = trials / 10
    mc = sys.maxint
    for t in range(trials):
        if t % ten_percent == 0:
            print(t * ten_percent, '%')
        _, _, trial_mc = compute_min_cut(al)
        if trial_mc < mc:
            mc = trial_mc
            print(mc)
