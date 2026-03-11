
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
            self.head = None
            self.tail = None
        
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head = Node(data, next=(self.head))
            (self.head).next.prev = self.head

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data, prev=self.tail)
            self.tail = self.tail.next
    
    def remove(self):
        if self.head == None or self.tail == None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            (self.head).prev = None
        
    def remove_end(self):
        if self.head == None or self.tail == None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            
    def is_empty(self):
        return self.head == None or self.tail == None
    
    def length(self):
        if self.head == None or self.tail == None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            num = 1
            start = self.head
            while start.next != None:
                num += 1
                start = start.next
            return num
        
    def get(self):
        return self.head.data
    
    def full(self):
        res = []
        start = self.head
        while start.next != None:
            res.append(start.data)
            start = start.next
        res.append(start.data)
        return res
    
    def reverse_full(self):
        res = []
        reverse = self.tail
        while reverse.prev != None:
            res.append(reverse.data)
            reverse = reverse.prev
        res.append(reverse.data)
        return res
    
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
def main():
    data = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),  
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]
    
    uczelnie = LinkedList()
    uczelnie.append(data[0])
    uczelnie.append(data[1])
    uczelnie.append(data[2])
    uczelnie.add(data[3])
    uczelnie.add(data[4])
    uczelnie.add(data[5])
    print(uczelnie.full())
    print(uczelnie.reverse_full())
    print(uczelnie.length())
    uczelnie.remove()
    print((uczelnie.full())[0])
    print(uczelnie.reverse_full()[0])
    uczelnie.remove_end()
    print(uczelnie.full())
    print(uczelnie.reverse_full())
    uczelnie.destroy()
    print(uczelnie.is_empty())
    
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.add(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == '__main__':
    main()  