
class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ' : ' + str(self.value)
    
    
class ElementNotFound(Exception):
    pass
class FullListException(Exception):
    pass

class HashTable:
    def __init__(self, size: int, c1: int = 1, c2: int = 0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size

    def hashing(self, key: int|str) -> int:
        res = 0
        if type(key) == str:
            for c in key:
                res += ord(c)
        else:
            res = key 
        return res % self.size

    def conflict(self, elem: Element) -> int:
        index = self.hashing(elem.key)
        old_index = index
        for i in range(self.size):
            if self.tab[index] is None or self.tab[index] == 'DELETED':
                return index
            index = (old_index + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size
        raise FullListException('Nie ma miejsca')            
    
    def search(self, key: int|str) -> int|str:
        index = self.hashing(key)
        old_index = index
        for i in range(self.size):
            if self.tab[index] is None:
                raise ElementNotFound('Brak klucza')
            elif self.tab[index] == 'DELETED':
                index = (old_index + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size
                continue
            elif self.tab[index].key == key:
                return self.tab[index].value
            index = (old_index + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size
        raise ElementNotFound('Brak klucza')
        
    def insert(self, elem: Element):
        index = self.hashing(elem.key)
        if self.tab[index] is None or self.tab[index] == 'DELETED':
            self.tab[index] = elem
        elif self.tab[index].key == elem.key:
            self.tab[index] = elem
        else:
            index = self.conflict(elem)
            self.tab[index] = elem
    
    def remove(self, key: int|str):
        index = self.hashing(key)
        old_index = index
        for i in range(self.size):
            if self.tab[index] is None:
                raise ElementNotFound('Brak klucza')
            if self.tab[index] == 'DELETED':
                index = (old_index + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size
                continue
            if self.tab[index].key == key:
                self.tab[index] = 'DELETED'
                return
            index = (old_index + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size
        raise ElementNotFound('Brak klucza')
    
    def __str__(self):
        res = []
        for i in range(self.size):
            if self.tab[i] is None:
                res.append('None: None')
            else:
                res.append(str(self.tab[i]))
        return '{' + ', '.join(res) + '}'
    
def test_1(size: int, c1: int, c2: int):
    test = HashTable(size, c1, c2)
    key = [i for i in range(1, 16)]
    key[5], key[6] = 18, 31
    val = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for k, v in zip(key, val):
        try:
            test.insert(elem=Element(key=k, value=v))
        except FullListException:
            print('Brak miejsca')
    print(test)

    print(test.search(key=5))
    
    try:
        print(test.search(key=14))
    except ElementNotFound:
        print('Brak klucza')

    test.insert(elem=Element(key=5, value='Z'))
    print(test.search(key=5))
    test.remove(key=5)
    print(test)
    
    try:
        print(test.search(key=31))
    except ElementNotFound:
        print('Brak klucza')
    try:
        test.insert(elem=Element(key='test', value='W'))
    except FullListException:
        print('Brak miejsca')
    print(test)

def test_2(size: int, c1: int, c2: int):
    test = HashTable(size, c1, c2)
    key = [(13 * i) for i in range(1, 16)]
    val = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for k, v in zip(key, val):
        try:
            test.insert(elem=Element(key=k, value=v))
        except FullListException:
            print('Brak miejsca')
    print(test)
    

def main():
    test_1(13, c1=1, c2=0)
    test_2(13, c1=0, c2=1)
    test_1(13, c1=0, c2=1)
    
if __name__ == '__main__':
    main()
    
    