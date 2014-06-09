__author__ = 'cman'


class AdjacencyList:

    def __init__(self, edges=[]):
        self.edges = {}
        self.vertices = set()
        for tail, head in edges:
            self.add_edge(tail, head)

    def add_edge(self, tail, head):
        edges = self.edges.setdefault(tail, [])
        edges.append((tail, head))
        edges = self.edges.setdefault(head, [])
        edges.append((tail, head))
        self.vertices.add(head)
        self.vertices.add(tail)

    def _dfs(self, start=None, visited=set(), backward=False, finishing={}, time=1):
        forward = not backward
        if start is None:
            start = self._start()
        if start is not None:
            stack = [start]
            while len(stack) > 0:
                v = stack[-1]
                if v not in visited:
                    visited.add(v)
                finished = True
                for tail, head in self.edges.get(v, []):
                    if backward and head == v:
                        # head is the tail when traversing backward
                        head = tail
                    elif forward and tail == v:
                        pass
                    else:
                        continue
                    if head not in visited:
                        stack.append(head)
                        finished = False
                        break
                if finished:
                    finishing[v] = time
                    time += 1
                    stack.pop()
        return time

    def dfs_loop(self, ordering_fn, backward=False):
        # keep track of how many nodes are 'finished' - this corresponds to the size of SCCs
        sizes = [0]
        visited = set()
        finishing = {}
        time = 1
        for tail in ordering_fn(self.vertices):
            if tail not in visited:
                time = self._dfs(tail, visited, backward, finishing, time)
                sizes.append(len(visited))
        return finishing, [sizes[i] - sizes[i - 1] for i in range(1, len(sizes))]

    def kasaraju(self):
        finishing, _ = self.dfs_loop(self.descending, True)

        def _finishing_times(vertices):
            return sorted(vertices, key=lambda v: -finishing[v])
        _, sizes = self.dfs_loop(_finishing_times)
        return sizes

    def descending(self, vertices):
        return sorted(vertices, reverse=True)

    def _start(self):
        for k in self.edges.keys():
            return k


if __name__ == '__main__':
    edges = []
    with open('assignment_four.input') as f:
        for line in f:
            edges.append(tuple([int(v.strip()) for v in line.split()]))
    al = AdjacencyList(edges)
    scc_sizes = al.kasaraju()

    print(','.join([str(scc) for scc in sorted(scc_sizes, reverse=True)]))
