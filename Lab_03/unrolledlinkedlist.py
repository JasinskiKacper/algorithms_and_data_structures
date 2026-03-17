
NODE_SIZE = 6

class UnrolledLinkedList:
    def __init__(self):
        self.head = None

    def get(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

class Node:
    def __init__(self):
        self.size = NODE_SIZE
        self.tab = [None for i in range(NODE_SIZE)]
        self.fill = 0
        self.next = None

    def add(self, value: int, index: int):
        if index >= self.fill:
            self.tab[index] = value
            self.fill += 1
        else:
            temp = self.tab[index]
            self.tab[index] = value
            for i in range(index, self.fill):
                temp0 = self.tab[(i + 1)]
                self.tab[i + 1] = temp
                temp = temp0
            self.fill += 1

    def remove(self, index: int):
        for i in range(index, self.fill):
            if (i + 1) < self.fill:
                temp = self.tab[i + 1]
            else:
                temp = None
            self.tab[i] = temp
        self.fill -= 1
            

def main():
    test = Node()
    test.add(value=0, index=0)
    test.add(value=1, index=0)
    test.add(value=2, index=0)
    test.add(value=3, index=1)
    test.add(value=4, index=1)
    test.add(value=5, index=1)
    test.remove(1)
    print(test.tab)

if __name__ == '__main__':
    main()