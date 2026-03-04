from copy import deepcopy

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

    # Matrix determinant by chio method
    def det_2x2(self) -> int:
        if self.size() != (2, 2):
            return None
        return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])

    def chio_method(self) -> 'Matrix':
        if self.size()[0] != self.size()[1]:
            return None
        
        if self.size() == (2, 2):
            return self.det_2x2()
        
        n = self.size()[0]
        matrix = Matrix((n - 1, n - 1))
        
        copy_matrix = deepcopy(self.__matrix__)
        swap = None
        sign = 1
        if self[0][0] == 0:
            for row in range(0, n):
                if copy_matrix[row][0] != 0:
                    swap = row
                    copy_matrix[0], copy_matrix[swap] = copy_matrix[swap], copy_matrix[0]
                    break
            if swap == None:
                return 0
            sign = -1

        fac = sign / ((copy_matrix[0][0]) ** (n - 2))

        for i in range(0, n - 1):
            for j in range(0, n - 1):
                matrix_2x2 = Matrix([[copy_matrix[0][0], copy_matrix[0][j + 1]],
                                     [copy_matrix[i + 1][0], copy_matrix[i + 1][j + 1]
                                      ]])
                matrix[i][j] = matrix_2x2.det_2x2()
        
        result = fac * matrix.chio_method()

        if result == 0:
            return 0
        
        return result

def transpose(matrix: Matrix) -> Matrix:
    rows, cols = matrix.size()
    result = Matrix((cols, rows))
    
    for i in range(0, rows):
        for j in range(0, cols):
            result[j][i] = matrix[i][j]
    
    return result

def main():
    m1 = Matrix([[5 , 1 , 1 , 2 , 3],
                 [4 , 2 , 1 , 7 , 3],
                 [2 , 1 , 2 , 4 , 7],
                 [9 , 1 , 0 , 7 , 0],
                 [1 , 4 , 7 , 2 , 2]])
    m2 = Matrix([[0 , 1 , 1 , 2 , 3],
                 [4 , 2 , 1 , 7 , 3],
                 [2 , 1 , 2 , 4 , 7],
                 [9 , 1 , 0 , 7 , 0],
                 [1 , 4 , 7 , 2 , 2]])
    m3 = Matrix([[0 , 0 , 0 , 0 , 0],
                 [4 , 2 , 1 , 7 , 3],
                 [2 , 1 , 2 , 4 , 7],
                 [9 , 1 , 0 , 7 , 0],
                 [1 , 4 , 7 , 2 , 2]])
    m4 = Matrix([[0 , 1 , 1 , 2 , 3],
                 [0 , 2 , 1 , 7 , 3],
                 [0 , 1 , 2 , 4 , 7],
                 [0 , 1 , 0 , 7 , 0],
                [0 , 4 , 7 , 2 , 2]])

    print(m1.chio_method())
    print(m2.chio_method())
    print(m3.chio_method())
    print(m4.chio_method())

if __name__ == '__main__':
    main()