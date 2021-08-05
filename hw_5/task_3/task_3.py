# Author: Viktor Mamontov
# Script for counting salary from a file

my_file = open('list.txt')
n = 0
sum = 0
for line in my_file:
    my_list = line.split(';')
    if int(my_list[1]) < 20000:
        print(my_list[0])
    sum += int(my_list[1])
    n += 1

print(f'Mean salary is {sum/n}')
my_file.close()
