# Author: Victor Mamontov
# Make class Worker and subclass Position

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_position(self):
        print(f'Position: {self.position}')

    def get_total_income(self):
        print(f'Total income: {sum(self._income.values())}')


position_1 = Position('Ivan', 'Petrov', 'Data Analyst', {'wage': 100000, 'bonus': 25000})
position_1.get_full_name()
position_1.get_position()
position_1.get_total_income()
