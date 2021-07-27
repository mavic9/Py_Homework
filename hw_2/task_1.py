# Author: Victor Mamontov
# Создать список и проверить тип его элементов

a = [1, 2.0, 'three', (1, 2, 3), False, {'Name': 'Bob', 'Age': 25}, [1, 2, 3]]

for i in a:
    print(f'{type(i)}', end=', ')
