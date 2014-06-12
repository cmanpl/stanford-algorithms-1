import sys

__author__ = 'cman'

"""
Notes:
- we assume that we can get from the start node s to all other vertices. If this is not true, we can
  treat the distance as infinity. A simple BFS could be useful to detect in advance which nodes are not
  reachable from s.
"""

INFINITY = sys.maxint

class AdjacencyList:

    def __init__(self, input_file=None, edges=[]):
        self.edges = {}
        self.vertices = set()
        if input_file is not None:
            with open(input_file) as f:
                for line in f:
                    if '#' in line:
                        continue
                    d = line.split()
                    tail = d[0]
                    for edge in d[1:]:
                        head, weight = edge.split(',')
                        self.add(int(tail), int(head), int(weight))
        for tail, head, weight in edges:
            self.add(tail, head, weight)

    def add(self, tail, head, weight):
        edges = self.edges.setdefault(tail, [])
        edges.append((head, weight))
        self.vertices.add(head)
        self.vertices.add(tail)

    def edgesFrom(self, vertex):
        return self.edges.get(vertex, [])

    def reachableFrom(self, vertex):
        reachable = set()
        if vertex not in self.edges:
            return reachable
        q = [vertex]
        while len(q) > 0:
            tail = q.pop(0)
            for head, weight in self.edgesFrom(tail):
                if head not in reachable:
                    q.append(head)
                    reachable.add(head)
        return reachable


def dijkstra(adjacencyList, start):
    distances = {v: INFINITY for v in adjacencyList.vertices}
    if start not in adjacencyList.vertices:
        return distances
    distances[start] = 0
    visited = set([start])
    reachable = adjacencyList.reachableFrom(start)
    if start in reachable:
        reachable.remove(start)
    while len(reachable) > 0:
        min = (None, INFINITY)
        for tail in visited:
            edges = adjacencyList.edgesFrom(tail)
            for head, weight in edges:
                if head in reachable:
                    distance = distances[tail] + weight
                    if distance < min[1]:
                        min = (head, distance)
        vertex, distance = min
        if vertex is not None:
            distances[vertex] = distance
            visited.add(vertex)
            reachable.remove(vertex)
    return distances


if __name__ == '__main__':
    al = AdjacencyList('assignment_five.input')
    result = dijkstra(al, 1)
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    answer = [result[v] for v in vertices]
    print(",".join([str(a) for a in answer]))

