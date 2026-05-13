from graph_mst import graph

class Vertex:
    def __init__(self, key: str|int):
        self.key = key
    
    def __eq__(self, other: 'Vertex') -> bool:
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __repr__(self) -> str|int:
        return self.key
            
class GraphList:
    def __init__(self):
        self.dict = {}

    def is_empty(self) -> bool:
        return len(self.dict) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        self.dict[vertex] = {}

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: int) -> None:
        self.dict[vertex1][vertex2] = edge
        self.dict[vertex2][vertex1] = edge

    def delete_vertex(self, vertex: Vertex) -> Vertex:
        neigh = list(self.neighbours(vertex))

        del self.dict[vertex]
        for vertex_id, edge in neigh:
            del self.dict[vertex_id][vertex]
        
        return vertex

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        del self.dict[vertex1][vertex2]
        del self.dict[vertex2][vertex1]

    def get_edge(self, vertex1: Vertex, vertex2: Vertex) -> int:
        return self.dict[vertex1][vertex2]

    def get_vertex(self, vertex_id: int) -> Vertex:
        return vertex_id

    def neighbours(self, vertex_id: Vertex) -> list[tuple]:
        return list(self.dict[vertex_id].items())

    def vertices(self) -> list:
        return self.dict.keys()

class MST:
    def __init__(self, graph: GraphList):
        self.graph = graph
        self.intree = {ver: False for ver in self.graph.vertices()}
        self.distance = {ver: float('inf') for ver in self.graph.vertices()}
        self.parent = {ver: None for ver in self.graph.vertices()}

        self.mst_graph = GraphList()
        for ver in self.graph.vertices():
            self.mst_graph.insert_vertex(ver)

    def prim(self) -> int:
        start = list(self.graph.vertices())[0]
        self.intree[start] = True
        self.distance[start] = 0

        current = start
        min_ver = None
        sum_dist = 0
        while False in self.intree.values():
            min_dist = float('inf')
            for neig, edge in self.graph.neighbours(current):
                if self.distance[neig] > edge and self.intree[neig] == False:
                    self.distance[neig] = edge
                    self.parent[neig] = current
                
            for ver, dist in self.distance.items():    
                if dist < min_dist and self.intree[ver] == False:
                    min_dist = dist
                    min_ver = ver

            current = min_ver
            self.intree[current] = True
            if self.parent[current] is not None:
                self.mst_graph.insert_edge(current, self.parent[current], min_dist)
            sum_dist += self.distance[current]

        return sum_dist
    
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


def main():
    test = GraphList()
    A = Vertex(key='A')
    B = Vertex(key='B')
    C = Vertex(key='C')
    D = Vertex(key='D')
    E = Vertex(key='E')
    F = Vertex(key='F')
    G = Vertex(key='G')
    H = Vertex(key='H')
    I = Vertex(key='I')
    J = Vertex(key='J')

    for ver in [A, B, C, D, E, F, G, H, I, J]:
        test.insert_vertex(ver)
        
    for ver1, ver2, edge in graph:
        test.insert_edge(Vertex(ver1), Vertex(ver2), edge)
        
    print(test.vertices())
    
    mst = MST(test)
    
    print(mst.intree)
    print(mst.distance)
    print(mst.parent)

    print(mst.prim())

    print(mst.intree)
    print(mst.distance)
    print(mst.parent)
    
    print(mst.mst_graph.dict)

    printGraph(mst.mst_graph)
if __name__ == '__main__':
    main()