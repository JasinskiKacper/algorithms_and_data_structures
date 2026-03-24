
class Node:
    def __init__(self, key: int, value: int|str):
        self.key = key
        self.value = value
        
class SkipList:
    def __init__(self, max_level: int):
        self.head = Node()
        self.max_level = max_level

    def search(self, key: int) -> int:
        pass

    def insert(self, key: int, value: int|str):
        pass

    def remove(self, key: int):
        pass

    def __str__(self) -> str:
        pass

def main():
    pass

if __name__ == '__main__':
    main()
