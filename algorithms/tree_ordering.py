__author__ = 'cman'


class Node:

    def __init__(self, name):
        self._nodes = []
        self._name = name

    def add_child(self, name):
        child = Node(name)
        self._nodes.append(child)
        return child

    def name(self):
        return self._name

    def children(self):
        return self._nodes


def build_tree():
    root = Node('component')
    tab1 = root.add_child('t1')
    tab1.add_child('c1')
    tab1.add_child('c2')
    tab1.add_child('c3')
    tab1.add_child('c4')
    tab2 = root.add_child('t2')
    tab2.add_child('c5')
    tab2.add_child('c6')
    tab2.add_child('c3')
    tab2.add_child('c4')
    return root


def child_ordering(node):
    stack = [node]
    while len(stack) > 0:
        n = stack.pop()
        for c in reversed(n.children()):
            if len(c.children()) == 0:
                print(c.name())
            else:
                stack.append(c)


if __name__ == '__main__':
    child_ordering(build_tree())
