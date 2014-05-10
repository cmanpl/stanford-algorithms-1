__author__ = 'cman'
import math


def multipy(a, b):
    la = None
    try:
        la, lb = len(a), len(b)
        wa, wb = len(a[0]), len(b[0])
        if la != wa:
            raise ValueError("First argument was not a square matrix")
        elif lb != wb:
            raise ValueError("Second argument was not a square matrix")
        elif la != lb and wa != wb:
            raise ValueError("Both matrices must have the same dimensions")
    except (TypeError, IndexError) as e:
        raise ValueError("Multiply expects two non-empty square matrices")
    logla = math.log(la, 2)
    if logla != math.floor(logla):
        lpad = 2 ** (int(math.floor(logla)) + 1)
        for i in range(lpad - la):
            for m in (a, b):
                m.append([0 for i in range(wa)])
        for rows in zip(a, b):
            for row in rows:
                row.extend([0 for i in range(lpad - la)])
    result = _multiply(a, b)
    return [row[:la] for row in result[:la]]


def _multiply(a, b):
    """
    [[A, B],  x [[E, F],
     [C, D]]     [G, H]]

    p1 = a0(b1-b3)
    p2 = (a0+a1)b3
    p3 = (a2+a3)b0
    p4 = a3(b2-b0)
    p5 = (a0+a3)(b0+b3)
    p6 = (a1-a3)(b2+b3)
    p7 = (a0-a2)(b0+b1)
    """
    if len(a) == 2:
        result = [
            [
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1]
            ],
            [
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1]
            ]
        ]
        return result
    else:
        a0, a1, a2, a3 = split_quadrants(a)
        b0, b1, b2, b3 = split_quadrants(b)
        p1 = _multiply(a0, subtract(b1, b3))
        p2 = _multiply(add(a0, a1), b3)
        p3 = _multiply(add(a2, a3), b0)
        p4 = _multiply(a3, subtract(b2, b0))
        p5 = _multiply(add(a0, a3), add(b0, b3))
        p6 = _multiply(subtract(a1, a3), add(b2, b3))
        p7 = _multiply(subtract(a0, a2), add(b0, b1))
        r0 = subtract(add(add(p5, p4), p6), p2)
        r1 = add(p1, p2)
        r2 = add(p3, p4)
        r3 = subtract(subtract(add(p1, p5), p3), p7)
        for i, row in enumerate(r1):
            r0[i] += row
        for i, row in enumerate(r3):
            r2[i] += row
        for row in r2:
            r0.append(row)
        return r0


def split_quadrants(a):
    """
    Returns 4 quadrants of a matrix a0-a4 starting in at the origin in a clockwise direction.

    Example:

    [[1, 1],
     [1, 1]]

    a0 = [[1]]
    a1 = [[1]]
    a2 = [[1]]
    a3 = [[1]]
    """
    a0, a1, a2, a3 = [[] for i in range(4)]
    l = len(a)
    lm = l / 2
    w = len(a[0])
    wm = w / 2
    a01 = a[:lm]
    a23 = a[lm:]
    for l in a01:
        a0.append(l[:wm])
        a1.append(l[wm:])
    for l in a23:
        a2.append(l[:wm])
        a3.append(l[wm:])
    return a0, a1, a2, a3


def add(a, b):
    return _add_or_subtract(a, b, op='add')


def subtract(a, b):
    return _add_or_subtract(a, b, op='sub')


def _add_or_subtract(a, b, op='add'):
    result = []
    for row in zip(a, b):
        cols = []
        result.append(cols)
        acols, bcols = row
        for i, col in enumerate(acols):
            if op == 'add':
                cols.append(acols[i] + bcols[i])
            elif op == 'sub':
                cols.append(acols[i] - bcols[i])
            else:
                raise ValueError("Unknown operation %s" % op)
    return result


def print_matrix(a):
    print('[')
    for row in a:
        print(', '.join([str(i) for i in row]))
    print(']')
