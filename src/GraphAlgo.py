from typing import List
from src.GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
from src.DiGraph import DiGraph
import json,math,random
from queue import PriorityQueue
import matplotlib.pyplot as pl
import sys
sys.setrecursionlimit(3000000)


#global varibaels
id=0
stack=[]
lows=dict()
ids=dict()
onStack=dict()
gloabl_list=[]
gloabl_lists=[]

class GraphAlgo (GraphAlgoInterface):
    """
    This class represents a directed weighted Graph Theory algorithms
    """

    def __init__(self,graph=DiGraph()):
        self.g=graph

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        This method loads a graph to this graph algorithm.
        @param file_name: file name
        @return: true - iff the graph was successfully loaded.
        """
        try:
            with open(file_name, 'r') as dataFromfile:
                json_format = json.load(dataFromfile)
            self.g = DiGraph()
            for vertex in json_format['Nodes']:
                position=vertex.get('pos')
                if position is not None:
                    pos = tuple(map(float,position.split(',')))
                    id = vertex.get('id')
                    self.g.add_node(id,pos)
                else:
                    id = vertex.get('id')
                    self.g.add_node(id)

            for edge in json_format['Edges']:
                self.g.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))

            return True
        except FileNotFoundError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves this weighted directed graph to the given file name.
        @param file_name - the file name.
        @return: true - iff the file was successfully saved.
        """
        Nodes=[]
        # {"pos":"35.204809147699756,32.105490531092435,0.0","id":47}
        #{"id": 0}
        for node in self.g.get_all_v().values():

            if node.get_pos() is None:
                Nodes.append({"id": node.get_key()})
            else:
                stri = str(node.get_pos()[0])+","+str(node.get_pos()[1])+","+str(node.get_pos()[2])
                Nodes.append({"pos":stri,"id": node.get_key()})
        Edges = []
        #{"src": 1, "dest": 3, "w": 1.8}
        for node in self.g.get_all_v().keys():
            for edge in self.g.all_out_edges_of_node(node).values():
                Edges.append({"src": edge.get_src(), "dest": edge.get_dest(), "w": edge.get_weight()})

        graph={'Nodes':Nodes,'Edges':Edges}
        try:
            with open(file_name,'w') as dataToFile:
                json.dump(graph,dataToFile)
            return True
        except FileNotFoundError:
            return False

    def __initi(self):
        for node in self.g.get_all_v().values():
            node.tag=0
            node.weight=math.inf
            node.info=""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if id1 not in self.g.get_all_v() or id2 not in self.g.get_all_v():
            return math.inf , []

        self.__initi()

        my_queue = PriorityQueue()

        node_src = self.g.get_all_v().get(id1)
        node_src.weight =0
        my_queue.put(node_src)

        while not my_queue.empty():
            node1= my_queue.get()
            for edge in self.g.all_out_edges_of_node(node1.get_key()).values():
                node2 =self.g.get_all_v().get(edge.get_dest())
                dest = edge.get_weight()  + node1.weight
                if dest < node2.weight:
                    node2.weight = dest
                    node2.info= node1.get_key()
                    my_queue.put(node2)

        node_dest = self.g.get_all_v().get(id2)
        if node_dest.weight is math.inf:
            return math.inf , []

        path_vertexs=[]
        path_vertexs.insert(0,id2)

        informition =  node_dest.info

        while informition != "":
            node = self.g.get_all_v().get(informition)
            path_vertexs.insert(0,node.get_key())
            informition = node.info

        return  node_dest.weight , path_vertexs

    def __init_component(self):
        for k in self.g.get_all_v().keys():
            lows.update({k:0})
            ids.update({k: 0})
            ids.update({k: False})

    def __help_component_dfs(self,at:int):
        global id, stack, lows, ids, onStack, gloabl_list, gloabl_lists
        id+=1
        stack.append(at)
        ids.update({at:id})
        lows.update({at:id})
        onStack.update({at:True})

        for to in self.g.all_out_edges_of_node(at).keys():
            if ids.get(to) == 0: self.__help_component_dfs(to)
            if onStack.get(to) is True: lows.update({at:min(lows.get(at),lows.get(to))})


        if ids.get(at) == lows.get(at):
            gloabl_list=[]
            while stack:
                node = stack.pop()
                gloabl_list.insert(0,node)
                onStack.update({node:False})
                lows.update({node:ids.get(at)})
                if node == at : break
            gloabl_lists.insert(0,gloabl_list)



    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        https://www.youtube.com/watch?v=wUgWX0nc4NY&feature=youtu.be
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if self.g is None or id1 not in self.g.get_all_v():
            return []

        global id,stack,lows,ids,onStack,gloabl_list,gloabl_lists
        id = 0
        stack = []
        lows = dict()
        ids = dict()
        onStack = dict()
        gloabl_list = []
        gloabl_lists = []
        self.__init_component()

        self.__help_component_dfs(id1)

        return gloabl_list


    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        Notes: If the graph is None the function returns an empty list []
        @return: The list all SCC
        """
        if self.g is None :
            return []

        global id, stack, lows, ids, onStack, gloabl_list, gloabl_lists
        id = 0
        stack = []
        lows = dict()
        ids = dict()
        onStack = dict()
        gloabl_list = []
        gloabl_lists = []
        self.__init_component()

        for x in self.g.get_all_v().keys():
            if ids.get(x) == 0 :
                self.__help_component_dfs(x)

        return gloabl_lists

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        :return: None
        """
        arraylis_x=[]
        arraylist_y=[]
        for node in self.g.get_all_v().values():
            if node.get_pos() is None:
                pos = (random.uniform(20,22), random.uniform(20, 22))
                node.set_pos(pos)
            arraylis_x.append(node.get_pos()[0])
            arraylist_y.append(node.get_pos()[1])

        n = [node_key for node_key in self.g.get_all_v().keys()]
        fig, ax = pl.subplots()
        ax.scatter(arraylis_x, arraylist_y)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (arraylis_x[p], arraylist_y[p]))

        pl.plot(arraylis_x,arraylist_y,".",color = "red")
        for node in self.g.get_all_v().keys():
            for edge in self.g.all_out_edges_of_node(node).values():
                node_src = self.g.get_all_v().get(edge.get_src())
                node_dest = self.g.get_all_v().get(edge.get_dest())

                x1=node_src.get_pos()[0]
                y1 = node_src.get_pos()[1]
                x2 = node_dest.get_pos()[0]
                y2 = node_dest.get_pos()[1]

                pl.arrow(x1, y1, (x2-x1), (y2-y1), shape='full', lw=0.05, length_includes_head=True, head_length= 0.025, head_width=0.05)

        pl.show()