

import random

def random_level(max_level: int, p: float = 0.5) -> int:
    lvl = 1
    while random.random() < p and lvl < max_level:
        lvl += 1
    return lvl

class Node:
    def __init__(self, key: int = None, value: int|str = None, level: int = None):
        self.key = key
        self.value = value
        self.level = level
        self.next = [None for _ in range(level)]


class SkipList:
    def __init__(self, max_level: int):
        self.max_level = max_level
        self.head = Node(level=self.max_level)

    def search(self, key: int) -> int|str:
        start = self.head
        lvl = self.max_level - 1

        while lvl >= 0:
            while start.next[lvl] is not None and start.next[lvl].key < key:
                start = start.next[lvl]
            lvl = lvl - 1
        if start.next[0] is not None and start.next[0].key == key:
            return start.next[0].value
        else:
            return None
        
    def insert(self, key: int, value: int|str) -> None:
        start = self.head
        update = [None for _ in range(self.max_level)]
 
        lvl = self.max_level - 1
        while lvl >= 0:
            while start.next[lvl] is not None and start.next[lvl].key < key:
                start = start.next[lvl]
            update[lvl] = start
            lvl -= 1
        if start.next[0] is not None and start.next[0].key == key:
            start.next[0].value = value
            return
        new_level = random_level(self.max_level)
        new_node = Node(key=key, value=value, level=new_level)
        for i in range(new_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def remove(self, key: int) -> None:
        start = self.head
        update = [None for _ in range(self.max_level)]
 
        lvl = self.max_level - 1
        while lvl >= 0:
            while start.next[lvl] is not None and start.next[lvl].key < key:
                start = start.next[lvl]
            update[lvl] = start
            lvl -= 1
 
        if start.next[0] is None or start.next[0].key != key:
            return None
 
        target = start.next[0]
        for i in range(target.level):
            update[i].next[i] = target.next[i]

    def __str__(self) -> str:
        result = []
        node = self.head.next[0]
        while node is not None:
            result.append(f"({node.key}:{node.value})")
            node = node.next[0]
        return "[" + ", ".join(result) + "]"
    
    def displayList_(self):
        node = self.head.next[0] 
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.next[0]
        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.value:2s}", end="")
                node = node.next[lvl]
            print()

def main():
    random.seed(42)
    test = SkipList(max_level=5)
    keys = [i for i in range(1, 16)]
    values = values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    for key, value in zip(keys, values):
        test.insert(key=key, value=value)
    print(test)
    print(test.search(key=2))
    test.insert(key=2, value='z')
    print(test.search(key=2))
    test.remove(key=5)
    test.remove(key=6)
    test.remove(key=7)
    print(test)
    test.insert(key=6, value='w')
    print(test)

if __name__ == '__main__':
    main()
