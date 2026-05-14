from graph_mst import graph

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, idx: int) -> int:
        while not self.root(idx):
            idx = self.parent[idx]

        return idx

    def root(self, idx: int) -> bool:
        return self.parent[idx] == idx

    def same_components(self, idx1: int, idx2: int) -> bool:
        return self.find(idx1) == self.find(idx2)

    def union_sets(self, idx1: int, idx2: int) -> None:
        if self.same_components(idx1, idx2):
            return None
        else:
            root1 = self.find(idx1)
            root2 = self.find(idx2)

            if self.size[root1] >= self.size[root2]:
                self.size[root1] += self.size[root2]
                self.parent[root2] = root1
            elif self.size[root1] < self.size[root2]:
                self.size[root2] += self.size[root1]
                self.parent[root1] = root2

def kruskal(graph: list[tuple]) -> UnionFind:
    graph = sorted(graph, key=lambda x : x[2])
    
    unique = set()
    for ver1, ver2, edge in graph:
        unique.add(ver1)
        unique.add(ver2)

    test = UnionFind(len(unique))
    res = []
    mst_sum = 0

    for ver1, ver2, edge in graph:
        ver1_asci = ord(ver1) - 65
        ver2_asci = ord(ver2) - 65
    
        if not test.same_components(ver1_asci, ver2_asci):
            test.union_sets(ver1_asci, ver2_asci)
            res.append((ver1, ver2, edge))
            mst_sum += edge

    return res, mst_sum

def main():
    test = UnionFind(6)

    print(test.parent)
    print(test.size)

    test.union_sets(1, 2)
    test.union_sets(2, 3)
    test.union_sets(4, 5)
    test.union_sets(3, 1)

    print(test.parent)
    print(test.size)

    print(kruskal(graph))

if __name__ == '__main__':
    main()