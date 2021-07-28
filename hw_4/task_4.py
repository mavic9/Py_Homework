# Author: Viktor Mamontov
# Print a list of non-repeated elements from random list

from random import randint as rnd

rnd_list = [rnd(1, 15) for i in range(20)]
print(rnd_list)  # show random list compared to the resulted one

my_list = [i for i in rnd_list if rnd_list.count(i) == 1]
print(my_list)
