from copy import deepcopy

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

    def __eq__(self, other: 'GraphMatrix') -> bool:
        return self.matrix == other.matrix
    
    def __mul__(self, other: 'GraphMatrix') -> 'GraphMatrix':
        if len(self.matrix[0]) != len(other.matrix):
            return None
        
        rows, cols = len(self.matrix), len(other.matrix[0])
        result = [[0] * cols for _ in range(rows)]
        res = GraphMatrix()
        res.matrix = result

        for i in range(0, rows): 
            for j in range(0, cols):
                 for k in range(0, len(self.matrix[0])):
                     res.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return res


def transpose(g: GraphMatrix) -> GraphMatrix:
    rows = len(g.matrix)
    cols = len(g.matrix[0])
    result = [[0] * rows for _ in range(cols)]
    res = GraphMatrix()
    res.matrix = result

    for i in range(0, rows):
        for j in range(0, cols):
            res.matrix[j][i] = g.matrix[i][j]
    
    return res

def ullmann_1(used: list = None,
            actual_row: int = 0,
            M: list[list] = None,
            G: GraphMatrix = None, 
            P: GraphMatrix = None,
            count: int = 0,
            iso: int = 0
            ) -> int:
    count += 1
    rows = len(P.matrix)
    cols = len(G.matrix[0])
    
    if actual_row == rows:
        m = GraphMatrix()
        m.matrix = M

        MG = m * G
        res = MG * transpose(m)
        if P == res:
            iso += 1
            return (count, iso)
        else:
            return (count, iso)

    if used is None:
        used = []
    if M is None:
        M = [[0] * cols for _ in range(rows)]
        
    for col in range(cols):
        if col not in used:
            used.append(col)
            M[actual_row] = [0] * cols
            M[actual_row][col] = 1

            count, iso = ullmann_1(used, actual_row + 1, M, G, P, count, iso)
            
            M[actual_row] = [0] * cols
            used.remove(col)
        
    return (count, iso)

def ullmann_2(used: list = None,
            actual_row: int = 0,
            M: list[list] = None,
            G: GraphMatrix = None, 
            P: GraphMatrix = None,
            count: int = 0,
            iso: int = 0
            ) -> int:
    count += 1
    rows = len(P.matrix)
    cols = len(G.matrix[0])
    
    if actual_row == rows:
        m = GraphMatrix()
        m.matrix = M

        MG = m * G
        res = MG * transpose(m)
        if P == res:
            iso += 1
            return (count, iso)
        else:
            return (count, iso)

    if used is None:
        used = []
    if M is None:
        M = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if len(P.neighbours(row)) <= len(G.neighbours(col)):
                    M[row][col] = 1
        
    for col in range(cols):
        if col not in used and M[actual_row][col] != 0:
            M_copy = deepcopy(M)
            used.append(col)
            M_copy[actual_row] = [0] * cols
            M_copy[actual_row][col] = 1

            count, iso = ullmann_2(used, actual_row + 1, M_copy, G, P, count, iso)
            
            M_copy[actual_row] = [0] * cols
            used.remove(col)
        
    return (count, iso)

def prune(M: GraphMatrix, P: GraphMatrix, G: GraphMatrix) -> GraphMatrix:
    rows = len(P.matrix)
    cols = len(G.matrix[0])

    changed = True
    while changed:
        changed = False
        for row in range(rows):
            for col in range(cols):
                if M[row][col] == 1:
                    for P_neig, _ in P.neighbours(row):
                        temp = None

                        for G_neig, _ in G.neighbours(col):
                            if M[P_neig][G_neig] != 0:
                                temp = G_neig          
                                break
                            
                        if temp is None:
                            M[row][col] = 0
                            changed = True
                            break

    return M

def ullmann_3(used: list = None,
            actual_row: int = 0,
            M: list[list] = None,
            G: GraphMatrix = None, 
            P: GraphMatrix = None,
            count: int = 0,
            iso: int = 0
            ) -> int:
    count += 1
    rows = len(P.matrix)
    cols = len(G.matrix[0])
    
    if actual_row == rows:
        m = GraphMatrix()
        m.matrix = M

        MG = m * G
        res = MG * transpose(m)
        if P == res:
            iso += 1
            return (count, iso)
        else:
            return (count, iso)

    if used is None:
        used = []
    if M is None:
        M = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if len(P.neighbours(row)) <= len(G.neighbours(col)):
                    M[row][col] = 1
        
    M_copy = deepcopy(M)
    M_prune = prune(M_copy, P, G)
    for col in range(cols):
        if col not in used and M_prune[actual_row][col] != 0:
            M_rek = deepcopy(M_prune)
            used.append(col)
            M_rek[actual_row] = [0] * cols
            M_rek[actual_row][col] = 1

            count, iso = ullmann_3(used, actual_row + 1, M_rek, G, P, count, iso)
            
            M_rek[actual_row] = [0] * cols
            used.remove(col)
        
    return (count, iso)

def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    
    G = GraphMatrix()
    P = GraphMatrix()

    for ver in ['A', 'B', 'C', 'D', 'E', 'F']:
        G.insert_vertex(ver)
        if ver in ['A', 'B', 'C']:
            P.insert_vertex(ver)
            
    for ver1, ver2, edge in graph_G:
        G.insert_edge(ver1, ver2, edge)
    for ver1, ver2, edge in graph_P:
        P.insert_edge(ver1, ver2, edge)
            
    print(G.matrix)
    print(P.matrix)

    print(ullmann_1(G=G, P=P))
    
    print(ullmann_2(G=G, P=P))

    print(ullmann_3(G=G, P=P))
    
if __name__ == '__main__':
    main()