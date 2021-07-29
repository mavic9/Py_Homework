from itertools import count, cycle

n = 50

my_list = [i for i in range(10)]
iterator = (count(start=0, step=1))
new_cycle = cycle(my_list)
new_list = [next(iterator) for i in range(n)]
my_cycle = [next(new_cycle) for i in range(n)]
print(new_list)
print(my_cycle)
