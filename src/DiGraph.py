
from src.GraphInterface import GraphInteface
from typing import Dict

from src.MyData import *
import sys
sys.setrecursionlimit(3000000)


class DiGraph(GraphInteface):
    """This class represents a directed weighted graph"""

    def __init__(self):
        self.__vertexs:Dict[int,NodeData]=dict()
        self.__edges :Dict[int,Dict[int,EdgeData]]=dict()
        self.__mc = 0
        self.__edge_size = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph.
        @return:the size vertex
        """

        return len(self.__vertexs)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph.
        @return: The size of edges in this graph.
        """
        return self.__edge_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased.
        @return: The current version of this graph.
        """
        return self.__mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID.
        @param pos: The position of the node.
        @return: True if the node was added successfully, False o.w.
        If the node id already exists the node will not be added.
        """
        if node_id not in self.__vertexs:
            nodedata= NodeData(node_id,pos)
            self.__mc+=1
            self.__vertexs.update({node_id:nodedata})
            self.__edges.update({node_id:dict()})
            return True
        else: return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge.
        @param id2: The end node of the edge.
        @param weight: The weight of the edge.
        @return: True if the edge was added successfully, False o.w.
        If the edge already exists or one of the nodes dose not exists the functions will do nothing.
        """
        if id1 is not id2 and id1 in self.__vertexs and id2 in self.__vertexs and id2 not in self.__edges.get(id1):
            #add edge
            edge=EdgeData(id1,id2,weight)
            self.__edges.get(id1).update({id2:edge})
            self.__mc += 1
            self.__edge_size+=1
            return True
        else: return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        If such an edge does not exists the function will do nothing
        """
        if node_id1 is not node_id2 and node_id1 in self.__vertexs and node_id2 in self.__vertexs and node_id2 in self.__edges.get(node_id1):
            #remove edge
            self.__edges.get(node_id1).pop(node_id2)
            self.__mc += 1
            self.__edge_size -= 1
            return True
        else: return False

    def get_all_v(self) -> dict:
        """
        Returns a dictionary of all the nodes in the graph, each node is represented using a pair.
        (node_id, node_data)
        """
        return self.__vertexs

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight).
        """
        answer:Dict[int,EdgeData]=dict()
        for x in self.__vertexs:
            if id1 in self.__edges.get(x):
                answer.update({x:self.__edges.get(x)[id1]})
        return answer

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary of all the nodes connected from node_id, each node is represented using a pair
        (other_node_id, weight)
        """

        return self.__edges.get(id1)



    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID.
        @return: True if the node was removed successfully, False o.w.
        If the node id does not exists the function will do nothing.
        """
        if node_id in self.get_all_v():
            len1 = len(self.all_in_edges_of_node(node_id))
            len2 = len(self.all_out_edges_of_node(node_id))
            len_in_out=len1+len2
            self.__mc+=len_in_out
            self.__edge_size-=len_in_out
            all_in=self.all_in_edges_of_node(node_id)
            for x in all_in:
                self.__edges.get(x).pop(node_id)
            self.__edges.pop(node_id)
            self.__vertexs.pop(node_id)
            self.__mc+=1
            return True
        else: return False

    def __repr__(self):
        return "Graph %s %s"%(self.__vertexs , self.__edges)