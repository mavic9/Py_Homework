# Author: Viktor Mamontov
# Print numbers divisible by 20 or 21

my_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(my_list)
