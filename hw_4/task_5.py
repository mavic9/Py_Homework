# Author: Viktor Mamontov
# Print a set from random list

import functools

my_list = [i for i in range(10, 1001, 2)]

my_sum = functools.reduce(lambda a, b: a*b, my_list)
print(my_sum)
