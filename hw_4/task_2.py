# Author: Viktor Mamontov
# Print elements in increasing order from random list

from random import randint as rnd

rnd_list = [rnd(1, 500) for i in range(10)]
print(rnd_list)  # show random list compared to the resulted one

new_list = [rnd_list[i] for i in range(1, len(rnd_list)) if rnd_list[i] > rnd_list[i-1]]
print(new_list)
