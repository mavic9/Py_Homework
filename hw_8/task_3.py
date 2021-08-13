# Author: Victor Mamontov
# Make own exception class for str type

class NewException(Exception):
    def __init__(self, message):
        self.message = message


new_list = []

while True:
    try:
        i = input('Enter number (or q to exit): ')
        if i == 'q':
            print(f'{new_list}')
            break
        if not i.isdigit():
            raise NewException('That was no number!!!')
        new_list.append(int(i))
    except NewException as err:
        print(err)
    else:
        print(new_list)
