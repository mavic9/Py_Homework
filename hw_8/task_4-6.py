# Author: Viktor Mamontov
# Make class Storage with subclasses of Office Equipment

# Class Storage store information about type of inventory and its' number
class Storage:
    all_storage = []
    inventory = {}

    def __init__(self, equipment, number):
        self.number = number
        self.equipment = equipment
        self.loading = {equipment: int(number)}
        Storage.inventory[self.equipment] = self.number

    def to_send(self):
        Storage.inventory.update(self.loading)
        return f'{Storage.inventory}'

    def __str__(self):
        message = ''
        for i, n in self.loading.items():
            message = f'{n} units of product {i}'
        return f'The storage has {message}'

    def check(self):
        message = ''
        for i, n in Storage.inventory.items():
            message += f'{i}: {n} units, '
        message = message[:-2]
        return f'The storage still has {message}.'


class Printer(Storage):
    def __init__(self, equipment, number):
        super().__init__(equipment, number)

    def new_doc(self):
        new_doc = ''
        for i in Storage.inventory.keys():
            new_doc += f'{i}, '
        new_doc = new_doc[:-2]
        return f'The storage contains following inventory: {new_doc}.'


class Computer(Storage):
    def __init__(self, equipment, number):
        super().__init__(equipment, number)

    @staticmethod
    def calculate(a, b):
        return a + b


class Table(Storage):
    def __init__(self, equipment, number):
        super().__init__(equipment, number)


new_table = Table('Table', 20)
new_printer = Printer('HP printer', 10)
new_computer = Computer('Lenovo', 20)
print(Storage.inventory)
print(new_table)
print(new_computer.calculate(5, 5))
print(new_printer.new_doc())


# New class Company uses data from the class Storage for inventory distribution
class Company:
    structure = {}

    def __init__(self, department):
        self.department = department

    def get_inventory(self, name, number):
        for i, n in Storage.inventory.items():
            try:
                if name == i:
                    if int(number) <= int(n):
                        Company.structure[self.department] = {i: number}
                        new_value = int(n) - int(number)
                        Storage.inventory[i] = new_value
                        return f'Department of {self.department} got {name} units of {number}'
                    else:
                        return f'There is no enough inventory!!!'
            except ValueError:
                print('You have put invalid message!!!')
        return f'There is no particular inventory at Storage!!!'


it_dep = Company('IT')
hr_dep = Company('HR')

inventory_list = list(Storage.inventory.keys())
name = input(f'Enter a product to order for IT department of Company: ')
number = input(f'Enter the number of product to buy: ')
print(it_dep.get_inventory(name, number))
print(f'The storage still has {Storage.inventory}')
print(f'Company updating: {Company.structure}')

name = input(f'Enter a product to order for HR department of Company: ')
number = input(f'Enter the number of product to buy: ')
print(hr_dep.get_inventory(name, number))
print(f'The storage still has {Storage.inventory}')
print(f'Company updating: {Company.structure}')
