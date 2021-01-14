import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.MyData import *


class TestGraphAlgo(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()

        p = (3, 4, 5)
        p2 = (3, 2, 4)
        p1 = (2, 3, 4)
        p3 = (3, 6, 4)
        self.graph.add_node(1, p)
        self.graph.add_node(2, p)
        self.graph.add_node(3, p1)
        self.graph.add_node(4, p2)
        self.graph.add_node(5, p3)

        self.graph.add_edge(1, 2, 600)
        self.graph.add_edge(2, 3, 600)
        self.graph.add_edge(3, 1, 600)
        self.graph.add_edge(3, 4, 600)
        self.graph.add_edge(4, 5, 600)
        self.graph.add_edge(5, 4, 600)
        self.algo = GraphAlgo(self.graph)


    def test_get_graph(self):
        self.assertTrue(self.graph, self.algo.get_graph())

    def test_save_to_json(self):
        self.assertFalse(self.algo.save_to_json("../stamcc/stamm"))
        self.assertTrue(self.algo.save_to_json("../data/test_check.json"))
        self.assertTrue(self.algo.save_to_json("test1.txt"))

    def test_load_and_save_from_json(self):
        self.assertTrue(self.algo.save_to_json("test_file"))
        self.assertTrue(self.algo.load_from_json('../data/A1'))
        self.assertTrue(self.algo.get_graph().v_size(), 20)
        self.assertTrue(self.algo.get_graph().e_size(), 12)
        self.assertTrue(self.algo.load_from_json('test_file'))
        self.assertTrue(self.algo.get_graph().v_size(), 2)
        self.assertTrue(self.algo.get_graph().e_size(), 1)

    def test_shortest_path(self):

        self.assertEqual((1200, [2,3,4]), self.algo.shortest_path(2, 4))
        self.assertEqual((600, [5,4]), self.algo.shortest_path(5,4))
        self.assertEqual((1200, [1,2,3]), self.algo.shortest_path(1,3))
        self.graph.add_node(6)
        self.graph.add_edge(6, 3, 10)
        self.assertEqual((610, [6,3,1]), self.algo.shortest_path(6,1))

    def test_connected_component(self):
        self.assertEqual(self.algo.connected_component(3), [3, 1, 2])
        self.assertEqual(self.algo.connected_component(4), [4,5])
        self.graph.add_node(6)
        self.assertEqual(self.algo.connected_component(6), [6])

    def test_connected_components_all(self):
        self.assertEqual(self.algo.connected_components(), [[1,2,3], [4, 5]])
        self.graph.add_node(6)
        self.assertEqual(self.algo.connected_components(), [[6],[1, 2, 3], [4, 5]])

    def test_dfs(self):
        self.assertEqual(self.algo.connected_components(), [[1,2,3], [4, 5]])
        self.graph.add_node(6)
        self.graph.add_node(7)
        self.graph.add_node(8)
        self.graph.add_edge(6, 3, 600)
        self.graph.add_edge(8, 7, 600)
        self.graph.add_edge(7, 8, 600)
        self.graph.add_edge(7, 5, 600)
        self.assertEqual(self.algo.connected_components(), [[7,8],[6],[1, 2, 3], [4, 5]])

    def test_graph_plot(self):
        self.algo.plot_graph()








