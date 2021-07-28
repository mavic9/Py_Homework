# Author: Viktor Mamontov
# Print elements in increasing order from random list

from random import randint as rnd

rnd_list = [rnd(1, 500) for i in range(10)]
print(rnd_list)


def my_sort(my_list):
    new_list = []
    n = 0
    while n < len(my_list)-1:
        if my_list[n + 1] > my_list[n]:
            new_list.append(my_list[n + 1])
        n += 1
    return new_list


my_list = my_sort(rnd_list)
print(my_list)
