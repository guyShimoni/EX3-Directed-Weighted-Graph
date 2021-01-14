class NodeData:
    """
    represents the set of operations applicable on a
    node (vertex) in a directed weighted graph.
    """
    def __init__(self, keyi: int, posi: tuple):
        self.__key = keyi
        self.__pos = posi
        self.tag = 0
        self.info = ""
        self.weight=0


    def get_key(self) ->int:
        return self.__key

    def get_pos(self)->tuple:
        """
        Returns the location of this node.
        :return: pos.
        """
        return self.__pos

    def set_pos(self,point:tuple):
        self.__pos = point

    def __lt__(self, other):
        my_weight = (self.weight,self.__key)
        other_weight = (other.weight,self.get_key())
        return   my_weight< other_weight

    def __repr__(self):
        #{"pos": "35.21213239225182,32.1077621697479,0.0", "id": 48}
        if self.__pos is None:
            return "{id:" + str(self.__key)+"}"
        return "{pos: "+str(self.__pos[0])+","+str(self.__pos[1])+","+str(self.__pos[2])+", id:" + str(self.__key)+"}"


class EdgeData:
    """
    represent an edge on the graph, each edge has src- the source node
    and dest- the destination node , each edge attached with a weight
    """

    def __init__(self, src: int, dest: int,w:float):
        self.__src=src
        self.__dest=dest
        self.__weight=w
        self.tag=0
        self.info=""


    def get_src(self) -> int:
        return self.__src

    def get_dest(self) -> int :
        return self.__dest

    def get_weight(self) -> float:
        return self.__weight

    def __repr__(self):
        # {"src":0,"w":1.3118716362419698,"dest":16}
        return "{src:" + str(self.__src)+",w:"+str(self.__weight)+",dest:"+str(self.__dest)+"}"