# Roulette game
import numpy as np

a = input("Spin roulette? (y/n): ")

while a == 'y':
    x = int(np.random.uniform(0,37))
    print(x)
    a = input("Spin roulette again? (y/n): ")
    if a != 'y':
        print('THe end of the game')
