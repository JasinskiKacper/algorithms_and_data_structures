
class Vertex:
    def __init__(self, key: str|int):
        self.key = key
    
    def __eq__(self, other: 'Vertex') -> bool:
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __repr__(self) -> str|int:
        return self.key

class Edge:
    def __init__(self, capacity: int, is_r: bool = False):
        if not is_r:
            self.capacity = capacity
            self.flow = 0
            self.r = self.capacity
            self.is_r = is_r
        else:
            self.capacity = 0
            self.flow = 0
            self.r = 0
            self.is_r = is_r
            
    def __repr__(self):
        return f'{self.capacity}c {self.flow}f {self.r}r {self.is_r}'
            
class GraphList:
    def __init__(self):
        self.dict = {}

    def is_empty(self) -> bool:
        return len(self.dict) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        self.dict[vertex] = {}

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge) -> None:
        self.dict[vertex1][vertex2] = edge
        self.dict[vertex2][vertex1] = Edge(0, True)

    def delete_vertex(self, vertex: Vertex) -> Vertex:
        neigh = list(self.neighbours(vertex))

        del self.dict[vertex]
        for vertex_id, edge in neigh:
            del self.dict[vertex_id][vertex]
        
        return vertex

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        del self.dict[vertex1][vertex2]
        del self.dict[vertex2][vertex1]

    def get_edge(self, vertex1: Vertex, vertex2: Vertex) -> Edge:
        return self.dict[vertex1][vertex2]

    def get_vertex(self, vertex_id: int) -> Vertex:
        return vertex_id

    def neighbours(self, vertex_id: Vertex) -> list[tuple]:
        return list(self.dict[vertex_id].items())

    def vertices(self) -> list:
        return self.dict.keys()

    def bfs(self, start: Vertex, end: Vertex) -> dict:
        visited = set()
        parent = {}
        queue = []
        
        queue.append(start)
        visited.add(start)
        parent[start] = None
        while queue:
            current = queue.pop(0)
            neig = self.neighbours(current)
            for neighbour, _ in neig:
                if self.get_edge(current, neighbour).r > 0 and neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    parent[neighbour] = current
            
            if current == end:
                return parent
    
        return parent

    def max_flow(self, start: Vertex, end: Vertex, parent: dict) -> int:
        if end not in parent:
            return 0
            
        current = end
        edge = self.get_edge(parent[current], current).r
        while current != start:
            temp_edge = self.get_edge(parent[current], current).r
            if temp_edge < edge:
                edge = temp_edge
    
            current = parent[current]
            
        return edge
    
    def augment(self, start: Vertex, end: Vertex, parent: dict, flow: int) -> None:
        current = end
        while current != start:
        
            edge = self.get_edge(parent[current], current)
            r_edge = self.get_edge(current, parent[current])
            if not edge.is_r:
                edge.flow += flow
                edge.r -= flow

                r_edge.r += flow
            else:
                r_edge.flow -= flow
                r_edge.r += flow

                edge.r -= flow

            current = parent[current]

    def ford(self, start: Vertex, end: Vertex) -> int:
        flow_sum = 0
        parent = self.bfs(start, end)

        while end in parent:
            flow = self.max_flow(start, end, parent)
            flow_sum += flow
            
            self.augment(start, end, parent, flow)

            parent = self.bfs(start, end)

        return flow_sum
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
def graph_1():
    test = GraphList()
    s = Vertex('s')
    u = Vertex('u')
    v = Vertex('v')
    t = Vertex('t')
    for i in [s, u, v, t]:
        test.insert_vertex(i)
        
    test.insert_edge(s, u, Edge(2))
    test.insert_edge(s, v, Edge(1))
    test.insert_edge(u, v, Edge(3))
    test.insert_edge(u, t, Edge(1))
    test.insert_edge(v, t, Edge(2))
    
    printGraph(test)
    print(test.ford(s, t))
    printGraph(test)

def graph_2():
    test = GraphList()
    s = Vertex('s')
    a = Vertex('a')
    c = Vertex('c')
    b = Vertex('b')
    d = Vertex('d')
    t = Vertex('t')

    for i in [s, a, c, b, d, t]:
        test.insert_vertex(i)

    test.insert_edge(s, a, Edge(16))
    test.insert_edge(s, c, Edge(13))
    test.insert_edge(a, c, Edge(10))
    test.insert_edge(a, b, Edge(12))
    test.insert_edge(c, d, Edge(14))
    test.insert_edge(b, c, Edge(9))
    test.insert_edge(d, b, Edge(7))
    test.insert_edge(b, t, Edge(20))
    test.insert_edge(d, t, Edge(4))

    printGraph(test)
    print(test.ford(s, t))
    printGraph(test)

def graph_3():
    test = GraphList()
    s = Vertex('s')
    a = Vertex('a')
    c = Vertex('c')
    b = Vertex('b')
    d = Vertex('d')
    e = Vertex('e')
    t = Vertex('t')

    for i in [s, a, c, b, d, e, t]:
        test.insert_vertex(i)

    test.insert_edge(s, c, Edge(3))
    test.insert_edge(s, a, Edge(3))
    test.insert_edge(d, a, Edge(1))
    test.insert_edge(c, d, Edge(2))
    test.insert_edge(c, e, Edge(6))
    test.insert_edge(e, t, Edge(9))
    test.insert_edge(d, t, Edge(1))
    test.insert_edge(b, s, Edge(3))
    test.insert_edge(b, c, Edge(1))
    test.insert_edge(b, d, Edge(2))
    test.insert_edge(a, b, Edge(4))

    printGraph(test)
    print(test.ford(s, t))
    printGraph(test)

def graph_4():
    test = GraphList()
    s = Vertex('s')
    a = Vertex('a')
    c = Vertex('c')
    b = Vertex('b')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    t = Vertex('t')

    for i in [s, a, c, b, d, e, f, t]:
        test.insert_vertex(i)

    test.insert_edge(s, a, Edge(3))
    test.insert_edge(a, b, Edge(4))
    test.insert_edge(b, c, Edge(5))
    test.insert_edge(c, t, Edge(6))
    test.insert_edge(f, t, Edge(3))
    test.insert_edge(e, f, Edge(2))
    test.insert_edge(d, e, Edge(2))
    test.insert_edge(s, d, Edge(2))
    test.insert_edge(a, f, Edge(3))

    
    printGraph(test)
    print(test.ford(s, t))
    printGraph(test)

def main():
    graph_1()
    graph_2()
    graph_3()
    graph_4()

if __name__ == '__main__':
    main()