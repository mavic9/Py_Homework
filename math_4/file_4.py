# All variants of 10 elements in 4 positions
import itertools

n = 0

for p in itertools.product('0123456789', repeat=4):
    # print(''.join(p))
    n += 1
print(n)

