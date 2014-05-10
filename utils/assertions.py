__author__ = 'cman'


def is_sorted(input, key=None):
    if key is None:
        test = zip(input, sorted(input))
    else:
        test = zip(input, sorted(input, key=key))
    for i, s in test:
        if i != s:
            return False
    return True