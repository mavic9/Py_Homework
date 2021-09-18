# test a probability of getting two zeros in a row in the roullete game
# the probability should be equal to (1/37)*(1/37)

import numpy as np
import itertools

n = 0

roulette = [i for i in range(0, 37, 1)]

for p in itertools.product(roulette, repeat=2):
    n += 1

p = 1/n
print(f'All possible variants of two starts in the roullets: {n}')
print(f'Probability of two zeros in a row: {p}')
print(f'(1/37)*(1/31) = {1/37*1/37}')
