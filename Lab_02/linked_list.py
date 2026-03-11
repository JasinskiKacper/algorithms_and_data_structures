class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None
        
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = Node(data)
        
    def remove(self):
        if self.head == None:
            return None
        self.head = (self.head).next
        
    
    def remove_end(self):
        if self.head == None:
            return None
        start = self.head
        if start.next == None:
            self.head = None
        else:
            while start.next.next != None:
                start = start.next
            start.next = None
            
    def is_empty(self):
        return self.head == None
    
    def length(self):
        num = 0
        if self.head == None:
            return num
        else:
            num = 1
            start = self.head
            while start.next != None:
                start = start.next
                num += 1
            return num
    
    def get(self):
        return (self.head).data
    
    def full(self):
        result = []
        start = self.head
        while start.next != None:
            result.append(start.data)
            start = start.next
        result.append(start.data)
        return result
        
class Node:
    def __init__(self, data, next = None):
        self.data = data 
        self.next = next

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
    print(uczelnie.length())
    uczelnie.remove()
    print((uczelnie.full())[0])
    uczelnie.remove_end()
    print(uczelnie.full())
    uczelnie.destroy()
    print(uczelnie.is_empty())
    
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.add(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())
    
if __name__ == '__main__':
    main()