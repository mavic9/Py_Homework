# Author: Viktor Mamontov
# Print a set from random list

from random import randint as rnd

rnd_list = [rnd(1, 15) for i in range(20)]
print(rnd_list)


def my_sort(my_list):
    my_list.reverse()
    k = 0
    # while loop removes all repeated elements in the list
    while k < len(my_list):
        while my_list.count(k) > 1:
            my_list.remove(k)
        k += 1

    my_list.reverse()
    return my_list


sorted_list = my_sort(rnd_list)
print(sorted_list)

# remove commenting signs # below for test
# print(len(sorted_list))
# print(set(rnd_list))
# print(len(rnd_list))
