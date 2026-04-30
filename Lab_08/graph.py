import polska

class Vertex:
    def __init__(self, key: str|int):
        self.key = key
    
    def __eq__(self, other: 'Vertex') -> bool:
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __repr__(self) -> str|int:
        return self.key

class GraphMatrix:
    def __init__(self, value: int = 0):
        self.matrix = [[]]
        self.list = []
        self.value = value
    def is_empty(self) -> bool:
        return len(self.list) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        if self.is_empty():
            self.list.append(vertex)
            self.matrix[0].append(self.value)
            return None
        
        self.list.append(vertex)

        for row in range(len(self.matrix)):
            self.matrix[row].append(self.value)        

        self.matrix.append([0 for _ in range(len(self.list))])

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: int) -> None:
        idx1 = self.list.index(vertex1)
        idx2 = self.list.index(vertex2)

        self.matrix[idx1][idx2], self.matrix[idx2][idx1] = edge, edge

    def delete_vertex(self, vertex: Vertex) -> Vertex:
        idx = self.list.index(vertex)

        self.matrix.pop(idx)
        self.list.pop(idx)
        for row in range(len(self.list)):
            self.matrix[row].pop(idx)

        return vertex

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        idx1 = self.list.index(vertex1)
        idx2 = self.list.index(vertex2)

        self.matrix[idx1][idx2], self.matrix[idx2][idx1] = 0, 0

    def get_edge(self, vertex1: Vertex, vertex2: Vertex) -> int:
        idx1 = self.list.index(vertex1)
        idx2 = self.list.index(vertex2)

        return self.matrix[idx1][idx2]

    def get_vertex(self, vertex_id: int) -> Vertex:
        return self.list[vertex_id]

    def neighbours(self, vertex_id: int) -> tuple|list[tuple]:
        res = []
        for i in range(len(self.matrix[vertex_id])):
            if self.matrix[vertex_id][i] != self.value:
                tup = (i, self.matrix[vertex_id][i])
                res.append(tup)

        return res

    def vertices(self) -> list:
        return [i for i in range(len(self.list))]

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

    def neighbours(self, vertex_id: Vertex) -> tuple|list[tuple]:
        return self.dict[vertex_id].items()

    def vertices(self) -> list:
        return self.dict.keys()

def main():
    test_m = GraphMatrix()
    test_l = GraphList()

    wojewodztwa = [] 
    for vertex1, vertex2 in polska.graf:
        wojewodztwa.append(vertex1)
        wojewodztwa.append(vertex2)

    unique = set(wojewodztwa)

    for uni in unique:
        test_m.insert_vertex(vertex=Vertex(key=uni))
        test_l.insert_vertex(vertex=Vertex(key=uni))

    for vertex1, vertex2 in polska.graf:
        test_m.insert_edge(vertex1=Vertex(key=vertex1), 
                           vertex2=Vertex(key=vertex2), edge=1)
        test_l.insert_edge(vertex1=Vertex(key=vertex1), 
                           vertex2=Vertex(key=vertex2), edge=1)

    test_m.delete_vertex(vertex=Vertex(key='K'))
    test_l.delete_vertex(vertex=Vertex(key='K'))
    
    test_m.delete_edge(vertex1=Vertex(key='W'), vertex2=Vertex(key='E'))    
    test_l.delete_edge(vertex1=Vertex(key='W'), vertex2=Vertex(key='E'))

    polska.draw_map(test_m)
    polska.draw_map(test_l)

if __name__ == '__main__':
    main()