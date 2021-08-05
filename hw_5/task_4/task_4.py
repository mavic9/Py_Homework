# Author: Viktor Mamontov
# Copy text with changes to another file

with open('file.txt') as my_file:
    my_list = ['Один', 'Два', 'Три', 'Четыре']
    n = 0
    new_lines = []
    for line in my_file:
        elements = line.split(' ')
        print(elements)
        elements[0] = my_list[n]
        new_lines += elements
        n += 1
        print(new_lines)

with open('new_file.txt', 'w+') as new_file:
    new_file.writelines(i + ' ' for i in new_lines)
