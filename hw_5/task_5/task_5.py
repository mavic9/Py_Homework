# Author: Viktor Mamontov
# Count a sum of numbers contained in a file

with open('my_file.txt', 'w+') as my_file:
    line = input('Enter numbers separated with spaces: ')
    my_file.write(line)

with open('my_file.txt') as my_file:
    n = 0
    for line in my_file:
        i = line.split(' ')

my_sum = 0
for x in i:
    a = int(x)
    my_sum += a
print(my_sum)
