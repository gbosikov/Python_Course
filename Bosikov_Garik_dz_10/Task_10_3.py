class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def _isinstance(self, inst):
        if not isinstance(inst, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        else:
            return True

    def __add__(self, other):
        if self._isinstance(other):
            return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self._isinstance(other):
            if self.cells <= other.cells:
                raise ValueError('недопустимая операция')
            else:
                return Cell(self.cells - other.cells)

    def __mul__(self, other):
        if self._isinstance(other):
            return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        if self._isinstance(other):
            return Cell(int(self.cells / other.cells))

    def __floordiv__(self, other):
        if self._isinstance(other):
            return Cell(int(self.cells // other.cells))

    def __str__(self):
        return 'Ячейки клетки: \n' + str(self.make_order())

    def make_order(self, n: int = 5) -> str:
        a = ''
        for i in range(1, self.cells+1):
            a += '*'
            if i % n == 0:
                a += '\n'

        return a


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)