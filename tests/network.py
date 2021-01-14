import networkx as nx
import json
import timeit


from src.GraphAlgo import GraphAlgo


def networkx(filename):

    with open(filename,'r') as file_read:
        obj=json.load(file_read)


    graph=nx.DiGraph()

    for x in obj.get('Nodes'):
        graph.add_node(int(x.get('id')))
    for x in obj.get('Edges'):
        graph.add_edge(int(x.get('src')),int(x.get('dest')),weight=float(x.get('w')))

    start=timeit.default_timer()
    print(list(nx.strongly_connected_components(graph)))
    stop = timeit.default_timer()
    print("time strongly_connected_components ",(stop-start))

    start = timeit.default_timer()
    print(nx.shortest_path(graph,source=0,target=3,weight="weight",method="dijkstra"))
    stop = timeit.default_timer()
    print("time shortest_path ",(stop-start))




def my_graph(filename):

    al=GraphAlgo()

    al.load_from_json(filename)

    start=timeit.default_timer()
    print(al.connected_components())
    stop = timeit.default_timer()
    print("time connected_components my_graph",(stop-start))

    start = timeit.default_timer()
    print(al.shortest_path(0,22))
    stop = timeit.default_timer()
    print("time shortest_path my_graph",(stop-start))

    start = timeit.default_timer()
    print(al.connected_component(0))
    stop = timeit.default_timer()
    print("time connected_component my_graph",(stop-start))
    print(al.plot_graph())

if __name__ == '__main__':
    networkx("../data/G_10_80_1.json")
    my_graph("../data/G_10_80_1.json")
