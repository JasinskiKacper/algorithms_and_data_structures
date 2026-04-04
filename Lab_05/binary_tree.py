
class Node:
    def __init__(self, key: int, 
                value: int|str, 
                left: 'Node' = None, 
                right: 'Node' = None
                ):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def search(self, key: int) -> int|str:
        if self.root == None:
            return None
        
        start = self.root
        while start.key != key:
            
            if start.key > key:
                start = start.left
            elif start.key < key:
                start = start.right
            
            if start is None:
                return None
            if start.key == key:
                return start.value
        
        return None
    
    def insert(self, nod: Node) -> None:
        if self.root == None:
            self.root = nod
        
        start = self.root
        while start.key != nod.key:
            
            if start.key > nod.key:
                if start.left is None:
                    start.left = nod
                else:
                    start = start.left
    
            elif start.key < nod.key:
                if start.right is None:
                    start.right = nod
                else:
                    start = start.right
    
            elif start.key == nod.key:
                start.value = nod.value
    
    def delete(self, key: int|str) -> None:
        if self.root == None:
            return None
            
        start = self.root
        prev = None
        while start.key != key:
            if start.key > key:
                if start.left is None:
                    return None
                else:
                    prev = start
                    start = start.left
            elif start.key < key:
                if start.right is None:
                    return None
                else:
                    prev = start
                    start = start.right
        
    # 0 Node
        if start.left is None and start.right is None:
            if prev.left == start:
                prev.left = None
            elif prev.right == start:
                prev.right = None
        
    # 1 Node 
        # Right
        elif start.left is None:
            if prev.right == start:
                prev.right, start.right = start.right, None
            elif prev.left == start:
                prev.left, start.right = start.right, None
        # Left
        elif start.right is None:
            if prev.right == start:
                prev.right, start.left = start.left, None
            elif prev.left == start:
                prev.left, start.left = start.left, None
                
    # 2 Nodes
        else:
            if prev is None:
                right_min = start.right
                temp_prev = right_min
                while right_min.left != None:
                    temp_prev = right_min
                    right_min = right_min.left

                if right_min.right is None:
                    if right_min != temp_prev:
                        start.key, start.value, temp_prev.left = right_min.key, right_min.value, None
                    else:
                        start.key, start.value, start.right = right_min.key, right_min.value, None
                elif right_min.right != None:
                    start.key, start.value = right_min.key, right_min.value
                    if right_min != temp_prev:
                        right_min.right, temp_prev.left = None, right_min.right
                    else:
                        start.right, right_min.right = right_min.right, None
            elif prev.left == start:
                right_min = start.right
                temp_prev = right_min
                while right_min.left != None:
                    temp_prev = right_min
                    right_min = right_min.left

                if right_min.right is None:
                    if right_min != temp_prev:
                        start.key, start.value, temp_prev.left = right_min.key, right_min.value, None
                    else:
                        start.key, start.value, start.right = right_min.key, right_min.value, None
                elif right_min.right != None:
                    start.key, start.value = right_min.key, right_min.value
                    if right_min != temp_prev:
                        right_min.right, temp_prev.left = None, right_min.right
                    else:
                        start.right, right_min.right = right_min.right, None

            elif prev.right == start:
                left_max = start.left
                temp_prev = left_max
                while left_max.right != None:
                    temp_prev = left_max
                    left_max = left_max.right

                if left_max.left is None:
                        if left_max != temp_prev:
                            start.key, start.value, temp_prev.right = left_max.key, left_max.value, None
                        else:
                            start.key, start.value, start.left = left_max.key, left_max.value, None
                elif left_max.right != None:
                        start.key, start.value = left_max.key, left_max.value
                        if left_max != temp_prev:
                            left_max.left, temp_prev.right = None, left_max.left
                        else:
                            start.left, left_max.left = left_max.left, None

    def print_as_list(self, node: Node) -> None:
        if node is None:
            return 
        self.print_as_list(node.left)
        print(f'{node.key} {node.value}', end=',')
        self.print_as_list(node.right)

    def print_tree(self) -> None:
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)
    
    def height(self, node: Node) -> int:
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)

        return max(left, right) + 1

def main():
    test = BinaryTree()
    node1 = Node(key=50, value='A')
    node2 = Node(key=15, value='B')
    node3 = Node(key=62, value='C')
    node4 = Node(key=5, value='D')
    node5 = Node(key=20, value='E')
    node6 = Node(key=58, value='F')
    node7 = Node(key=91, value='G')
    node8 = Node(key=3, value='H')
    node9 = Node(key=8, value='I')
    node10 = Node(key=37, value='J')
    node11 = Node(key=60, value='K')
    node12 = Node(key=24, value='L')

    for node in [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12]:
        test.insert(node)

    test.print_tree()
    test.print_as_list(test.root)

    print('\n\n')
    print(test.search(24))

    test.insert(Node(key=20, value='AA'))
    test.insert(Node(key=6, value='M'))
    test.delete(key=62)
    test.insert(Node(key=59, value='N'))
    test.insert(Node(key=100, value='P'))
    test.delete(key=8)
    test.delete(key=15)
    test.insert(Node(key=55, value='R'))
    test.delete(key=50)
    test.delete(key=5)
    test.delete(key=24)
    
    print(test.height(test.root))
    test.print_as_list(test.root)
    print('\n')
    test.print_tree()

if __name__ == '__main__':
    main()