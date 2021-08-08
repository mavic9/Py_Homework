# Author: Victor Mamontov
# Make class Matrix for matrix addition

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        my_matrix = ""
        for i in self.my_list:
            for n in i:
                my_matrix += f'{n:02} '
            my_matrix += '\n'
        return f'{my_matrix}'

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.my_list)):
            new_row = []
            for k in range(len(self.my_list[0])):
                new_row.append(self.my_list[i][k] + other.my_list[i][k])
            new_matrix.append(new_row)
        return Matrix(new_matrix)


list_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
list_2 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
list_3 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(list_1)
print(list_2)
print(list_3)
print(list_1 + list_2 + list_3)
