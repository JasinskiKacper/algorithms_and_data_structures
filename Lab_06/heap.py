
class Element:
    def __init__(self, prio: int, data : str):
        self.prio = prio
        self.data = data

    def __lt__(self, other) -> bool:
        return self.prio < other.prio
    def __gt__(self, other) -> bool:
        return self.prio > other.prio
        
    def __repr__(self) -> str:
        return str(self.prio) + ':' + str(self.data)

class Heap:
    def __init__(self):
        self.queue = []
        self.size = len(self.queue)
    
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    def left(self, i: int) -> int:
        return (2 * i) + 1
    def right(self, i: int) -> int:
        return (2 * i) + 2
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def peek(self) -> Element:
        if self.is_empty():
            return None
        
        return self.queue[0]
        
    def fixheap(self, i: int) -> None:
        left = self.left(i)
        right = self.right(i)
        
        while left < (self.size - 1):
            if right >= self.size:
                if self.queue[i] < self.queue[left]:
                    self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                break
    
            if self.queue[left] > self.queue[right]:
                if self.queue[i] < self.queue[left]:
                    self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                    i = left
                    left = self.left(i)
                else:
                    break
            else:
                if self.queue[i] < self.queue[right]:
                    self.queue[i], self.queue[right] = self.queue[right], self.queue[i]
                    i = right
                    right = self.right(i)
                else:
                    break

    def dequeue(self) -> Element:
        if self.is_empty():
            return None

        res = self.queue[0]

        self.queue[0], self.queue[(self.size - 1)] = self.queue[(self.size - 1)], self.queue[0] 
        self.size -= 1
    
        self.fixheap(0)
        return res
    
    def enqueue(self, elem: Element) -> None:
        if len(self.queue) == self.size:
            self.queue.append(elem)
            self.size += 1
        else:
            self.queue[self.size] = elem
            self.size += 1

        index = self.size - 1
        parent = self.parent(index)
        while self.queue[index] > self.queue[parent] or index == 0:
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
        
            index = parent
            parent = self.parent(index)
            if index == 0:
                break

    def print_tab(self):
        print('{', end=' ')
        print(*self.queue[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

def main():
    test = Heap()
    prios = [7, 5, 1, 2, 5, 3, 4, 8, 9]

    for p, ch in zip(prios, 'GRYMOTYLA'):
        test.enqueue(Element(prio=p, data=ch))
    
    test.print_tree(0, 0)
    test.print_tab()

    deleted = test.dequeue()
    print(deleted)
    print(test.peek())

    test.print_tab()
    print(deleted)

    petla = True
    while petla:
        stop = test.dequeue()
        print(stop)
        if stop is None:
            petla = False
    
    test.print_tab()

if '__main__' == __name__:
    main()