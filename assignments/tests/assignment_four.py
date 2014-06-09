__author__ = 'cman'


from assignments.four import assignment_four
import unittest


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(AssignmentFourTest)


class AssignmentFourTest(unittest.TestCase):

    def _get_eg_graph(self):
        al = assignment_four.AdjacencyList()
        al.add_edge(4, 7)
        al.add_edge(7, 1)
        al.add_edge(1, 4)
        al.add_edge(9, 7)
        al.add_edge(9, 3)
        al.add_edge(3, 6)
        al.add_edge(6, 9)
        al.add_edge(8, 6)
        al.add_edge(8, 5)
        al.add_edge(5, 2)
        al.add_edge(2, 8)
        return al

    def test_eg_from_class(self):
        al = self._get_eg_graph()
        expected = {1: 7, 2: 3, 3: 1, 4: 8, 5: 2, 6: 5, 7: 9, 8: 4, 9: 6}
        finishing, _ = al.dfs_loop(al.descending, True)
        self.assertEqual(finishing, expected)

    def test_kasaraju_eg_from_class(self):
        al = self._get_eg_graph()
        sizes = al.kasaraju()
        self.assertEqual(sizes, [3, 3, 3])

    def test_disconnected(self):
        al = assignment_four.AdjacencyList()
        al.add_edge(1, 2)
        al.add_edge(3, 4)
        al.add_edge(5, 6)
        al.add_edge(7, 8)
        self.assertEqual(al.kasaraju(), [1 for i in range(8)])
        al.add_edge(2, 1)
        al.add_edge(4, 3)
        al.add_edge(6, 5)
        al.add_edge(8, 7)
        self.assertEqual(al.kasaraju(), [2 for i in range(4)])

    def test_cycle(self):
        al = assignment_four.AdjacencyList()
        al.add_edge(1, 2)
        al.add_edge(2, 3)
        al.add_edge(3, 4)
        al.add_edge(4, 1)
        self.assertEqual(al.kasaraju(), [4])




if __name__ == '__main__':
    unittest.main()

