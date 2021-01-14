import unittest
from src.DiGraph import *


class TestDiGraph(unittest.TestCase):

    def setUp(self) -> None:
        """
        build the central graph for all the tests
        """
        self.graph = DiGraph()

        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_node(5)

        self.graph.add_edge(1, 2, 600)
        self.graph.add_edge(2, 3, 600)
        self.graph.add_edge(3, 1, 600)
        self.graph.add_edge(3, 4, 600)
        self.graph.add_edge(4, 5, 600)
        self.graph.add_edge(5, 4, 600)

    def test_v_size(self):
        self.assertEqual(5, self.graph.v_size())

    def test_e_size(self):
        self.assertEqual(6, self.graph.e_size())

    def test_get_mc(self):
        self.assertEqual(11, self.graph.get_mc())

    def test_removeEdge(self):
        self.graph.remove_edge(3, 1)
        self.graph.remove_edge(2, 3)
        self.graph.remove_edge(5, 4)
        self.assertEqual(3, self.graph.e_size())
        self.graph.add_edge(3, 1, 1.67)
        self.assertEqual(4, self.graph.e_size())

    def test_removeNode(self):
        self.graph.remove_node(1)
        self.graph.remove_node(3)
        self.graph.remove_node(1)
        self.assertEqual(3, self.graph.v_size())

    def test_add_node(self):
        self.graph.add_node(6)
        self.graph.add_node(7)
        self.graph.add_node(8)
        self.graph.add_node(8)
        self.assertEqual(8, self.graph.v_size())

    def test_all_in_edges_of_node(self):
        self.assertTrue(len(self.graph.all_in_edges_of_node(1)) == 1)
        self.assertTrue(len(self.graph.all_in_edges_of_node(2)) == 1)
        self.graph.add_node(6)
        self.graph.add_edge(6,3,5.5)
        self.assertTrue(len(self.graph.all_in_edges_of_node(3)) == 2)

    def test_all_out_edges_of_node(self):
        self.assertTrue(len(self.graph.all_out_edges_of_node(2)) == 1)
        self.assertTrue(len(self.graph.all_out_edges_of_node(4)) == 1)
        self.assertTrue(len(self.graph.all_out_edges_of_node(3)) == 2)





