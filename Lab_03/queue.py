
class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [None for i in range(self.size)]
        self.i_save = 0
        self.i_read = 0
        
    def is_empty(self) -> bool:
        return self.i_save == self.i_read
        
    def peek(self) -> int:
        if self.is_empty():
            return None
        else:
            return self.queue[self.i_read]
        
    def dequeue(self) -> int:
        if self.is_empty():
            return None
        else:
            res = self.queue[self.i_read]
            self.queue[self.i_read] = None
            self.i_read = (self.i_read + 1) % self.size
            return res
        
    def enqueue(self, value: int):
        self.queue[self.i_save] = value
        self.i_save = (self.i_save + 1) % self.size

        if self.i_save == self.i_read:
            new_queue = [None for i in range(2 * self.size)]

            for i in range(self.size):
                new_queue[i] = self.queue[self.i_read]
                self.i_read = (self.i_read + 1) % self.size
                    
            self.queue = new_queue
            self.i_save = self.size
            self.i_read = 0
            self.size = 2 * self.size
    
    def __str__(self) -> str:
        if self.is_empty():
            return '[]'
        
        idx = self.i_read
        res = []
        while self.queue[idx] != None:
            res.append(self.queue[idx])
            idx = (idx + 1) % self.size
        
        return str(res)

    def to_list(self) -> list:
        return self.queue        
        
def main():
    test = Queue()
    test.enqueue(0)
    test.enqueue(1)
    print(test.dequeue())
    print(test.peek())
    test.enqueue(2)
    test.enqueue(3)
    test.enqueue(4)
    print(test.dequeue())
    print(test)
    test.enqueue(5)
    test.enqueue(6)
    test.enqueue(7)
    test.enqueue(8)
    print(test)
    while not test.is_empty():
        print(test.dequeue())
    print(test)
    
if __name__ == '__main__':
    main()