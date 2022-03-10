from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        check_len = [len(row) for row in matrix]
        if max(check_len) != min(check_len) or len(matrix) < 2:
            raise ValueError('fail initialization matrix')

    def __str__(self):
        a = ''
        for row in self.matrix:
            a += '|'
            for el in row:
                a += ' ' + str(el)
            a += ' |\n'
        return a

    def __add__(self, other):
        if isinstance(other, Matrix):
            a = self.matrix.copy()
            for i, row in enumerate(self.matrix):
                for j, val in enumerate(row):
                    a[i][j] = val + other.matrix[i][j]

            return Matrix(a)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """