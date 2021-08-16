# Author: Victor Mamontov
# Make own exception for zero division

class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    new_div = input('Enter two numbers for division separated with space: ').split(' ')
    a = int(new_div[0])
    b = int(new_div[1])
    if int(new_div[1]) == 0:
        raise Error('Can not divide at zero!!!')
except ValueError:
    print('That was no number type!!!')
except IndexError:
    print('You should enter two numbers at least!!!')
except Error as err:
    print(err)
else:
    result = a / b
    print(f'The result of division: {result}')
