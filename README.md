## EX3-OOP
Directed Weighted Graph

This project is about weighted directed graph with graph theory algoritms (Dijkstra, DFS..).
there is implemention of a directed weighted graph which functions such as add new node to the graph , finds all the Strongly Connected Component and more.
we implement graphs according to the json format.
In addition, we compared two different languages of development (Python and Java).
We compared Ex2 which works on graphs in java, and Ex3 in Python (development of identical graphs in different languages).

### MyData
is a class implements the node_data and the edge_data interface and create a new type of object,
is designed to create a vertex and edge in the graph for the class DiGraph .

### DiGraph
This class implements the interface of GraphAlgoInterface. responsible for all vertices and the edge of the graph it contains a number of operations like deleting and adding a vertex and edge and comparison of graphs, in addition it represents the structure of the graph. we chose dictionary data structure in Python with an O(1) time, the graph changes would be made quickly, even when it comes to a graph with A lots of nodes.

### GraphAlgo
This class implements the interface of GraphAlgoInterface.
this class implements algorithms that can be run on the graph, responsible for executing algorithms on the graph like returns the shortest path between two nodes using Dijkstra's Algorithm, save and load a graph from json,and more.

test_DiGraph- checks the integrity of the graph.

test_GraphAlgo- tests the algorithms that work.

The methods:

addNode- Adds a node to the graph.

add edge-Adds an edge to the graph.

removeNode- remove nodes from the graph.

removeEdge-remove edge from the graph.

save()- Saving the graph into a file in json format

load()- Loading a graph from a file in json format

shortestPath()-Returns the shortest path between two nodes using Dijkstra's Algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

connected_component-Finds the Strongly Connected Component(SCC) that node is a part of.
(https://www.youtube.com/watch?v=wUgWX0nc4NY&feature=youtu.be) 
