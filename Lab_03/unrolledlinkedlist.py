
NODE_SIZE = 6

class UnrolledLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return None
        start = self.head
        while index >= start.fill:
            index = index - start.fill
            start = start.next
        return start.tab[index]
        
    def insert(self, value: int, index: int):
        if self.head is None:
            self.head = Node()
            self.head.add(value, 0)
        else:
            start = self.head
            while index > start.fill:
                if start.next == None:
                    index = start.fill
                    break
                if index >= start.fill:
                    index -= start.fill
                    start = start.next

            if start.fill == NODE_SIZE:
                new_node = Node()
                mid = NODE_SIZE // 2
                for i in range(mid, NODE_SIZE):
                    new_node.tab[i - mid] = start.tab[i]
                    start.tab[i] = None
                new_node.fill = NODE_SIZE - mid
                start.fill = mid
                new_node.next = start.next
                start.next = new_node
                if index <= start.fill:
                    start.add(value, index)
                else:
                    new_node.add(value, index - start.fill)
            else:
                start.add(value, index)
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
            self.tab[self.fill] = value
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
    test = UnrolledLinkedList()
    for i in range(1, 11):
        test.insert(i, 999) 
    print(test.head.tab, test.head.fill)
    print(test.head.next.tab, test.head.next.fill)

if __name__ == '__main__':
    main()