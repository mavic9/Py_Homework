# Author: Victor Mamontov
# Make class Cell for operations

class Cell:
    def __init__(self, chambers):
        self.chambers = chambers

    def __str__(self):
        return f"The cell contains {self.chambers} chambers"

    def __add__(self, other):
        return Cell(self.chambers + other.chambers)

    def __sub__(self, other):
        if self.chambers >= other.chambers:
            return Cell(self.chambers - other.chambers)
        else:
            return f"Error: The value of the first cell must be larger than the second one!!!"

    def __mul__(self, other):
        return Cell(self.chambers * other.chambers)

    def __truediv__(self, other):
        return Cell(round(self.chambers // other.chambers))

    def make_order(self, order):
        my_order = ''
        for i in range(self.chambers // order):
            my_order += '*' * order + '\n'
        my_order += (self.chambers % order) * '*' + '\n'
        return f'{my_order}'


cell_1 = Cell(15)
cell_2 = Cell(25)
cell_3 = Cell(10)
print(cell_1 + cell_2)
print(cell_2 / cell_1)
print(cell_3 - cell_1)
print(cell_1 * cell_3)
print(cell_1.make_order(5))
print(cell_2.make_order(6))
print(cell_3.make_order(3))
