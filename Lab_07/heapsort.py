import random
import time

# === Element and Heap ===
class Element:
    def __init__(self, prio: int, data : str = None):
        self.prio = prio
        self.data = data

    def __lt__(self, other) -> bool:
        return self.prio < other.prio
    def __gt__(self, other) -> bool:
        return self.prio > other.prio
        
    def __repr__(self) -> str:
        return str(self.prio) + ':' + str(self.data)

class Heap:
    def __init__(self, lst: list = None):
        if lst == None:
            self.queue = []
            self.size = len(self.queue)

        else:
            self.queue = lst
            self.size = len(self.queue)
    
            start_idx = self.parent(self.size - 1)
            for i in range(start_idx + 1):
                self.fixheap(start_idx - i)

    def heapsort(self):
        original_size = self.size
        for _ in range(original_size):
            self.dequeue()
            
        self.size = original_size
            
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
        
        while left < self.size:
            if right >= self.size:
                if self.queue[i] < self.queue[left]:
                    self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                break
    
            if self.queue[left] > self.queue[right]:
                if self.queue[i] < self.queue[left]:
                    self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                    i = left
                    left = self.left(i)
                    right = self.right(i)
                else:
                    break
            else:
                if self.queue[i] < self.queue[right]:
                    self.queue[i], self.queue[right] = self.queue[right], self.queue[i]
                    i = right
                    left = self.left(i)
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

# === Swap and Shift sort ===
def swap_sort(lst: list[Element]) -> list[Element]:
    for i in range(len(lst)):
        idx = i
        for j in range(i, len(lst)):
            if lst[j].prio < lst[idx].prio:
                idx = j
    
        lst[i], lst[idx] = lst[idx], lst[i]
                
    return lst

def shift_sort(lst: list[Element]) -> list[Element]:
    res = lst.copy()

    for i in range(len(lst)):
        idx = i
        for j in range(i, len(lst)):
            if res[j].prio < res[idx].prio:
                idx = j
            
        minimum = res.pop(idx)
        res.insert(i, minimum)

    return res
# === Tests ===
def test1():
    # === Heapsort ===
    tuples = [
        (5,'A'), 
        (5,'B'), 
        (7,'C'), 
        (2,'D'), 
        (5,'E'), 
        (1,'F'), 
        (7,'G'), 
        (5,'H'), 
        (1,'I'), 
        (2,'J')
        ]
    lst = [Element(prio=prio, data=data) for prio, data in tuples]
    test = Heap(lst)
    test.print_tab()
    test.print_tree(0, 0)
    test.heapsort()
    test.print_tab()
    print('NIESTABILNE')

    # === Swap and shift sort ===
    lst_s = [Element(prio=prio, data=data) for prio, data in tuples]
    
    print(lst_s)
    print(swap_sort(lst_s))
    print('NIESTABILNE')
    lst_s = [Element(prio=prio, data=data) for prio, data in tuples]
    print(shift_sort(lst_s))
    print('STABILNE')

def test2():
    tab = [int(random.random() * 100) for _ in range(10000)]
    
    lst = [Element(prio=prio) for prio in tab]
    # === Heap sort ===
    t_start = time.perf_counter()
    test = Heap(lst)
    test.heapsort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    lst = [Element(prio=prio) for prio in tab]
    # === Swap sort ===
    t_start = time.perf_counter()
    swap_sort(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    lst = [Element(prio=prio) for prio in tab]
    # === Shift sort ===
    t_start = time.perf_counter()
    shift_sort(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def main():
    
    choice = int(input('Ktory test wybierasz 1 czy 2?\n'))
    if choice == 1:
        test1()
    elif choice == 2:
        test2()
    else:
        print('Zla liczba')
        main()



if '__main__' == __name__:
    main()