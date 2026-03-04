


class Matrix:
    def __init__(self, __matrix__: tuple|list[list[int]], number: int = 0):
        if isinstance(__matrix__, tuple):
            temp_matrix = [[number for j in range(0, __matrix__[1])] for i in range(0, __matrix__[0])]
            self.__matrix__ = temp_matrix
        else:
            self.__matrix__ = __matrix__

    def size(self) -> tuple[int, int]:
        return (len(self.__matrix__), len(self.__matrix__[0]))
        
    def __getitem__(self, index: int) -> int|list[int]:
        return self.__matrix__[index]
    
    def __eq__(self, other: 'Matrix') -> bool:
        return self.__matrix__ == other.__matrix__
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.size() != other.size():
            return None
        
        rows, cols = self.size()
        result = Matrix((rows, cols))

        for row in range(0, rows):
            for col in range(0, cols):
                result[row][col] = self[row][col] + other[row][col]
        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.size()[1] != other.size()[0]:
            return None
        
        rows, cols = self.size()[0], other.size()[1]
        result = Matrix((rows, cols))

        for i in range(0, rows): 
            for j in range(0, cols):
                 for k in range(0, self.size()[1]):
                     result[i][j] += self[i][k] * other[k][j]
        return result

    def __str__(self) -> str:
        string = '\n'.join([str(x) for x in self.__matrix__])
        return string.replace(',', '').replace('[', '| ').replace(']', ' |')

def transpose(matrix: Matrix) -> Matrix:
    rows, cols = matrix.size()
    result = Matrix((cols, rows))
    
    for i in range(0, rows):
        for j in range(0, cols):
            result[j][i] = matrix[i][j]
    
    return result
    

def main():
    m1 = Matrix(
        [[1, 0, 2],
        [-1, 3, 1]]
        )
    
    m2 = Matrix(
        [[3, 1],
         [2, 1],
         [1, 0]]
         )

    print(m1)
    print(transpose(m1))
    print(m1 + Matrix((2,3), number=1))
    print(m1 * m2)

if __name__ == '__main__':
    main()