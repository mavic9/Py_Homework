# 100 sums of 100 random numbers

import numpy as np
import matplotlib.pyplot as plt

a = []
for i in range(100):
    x = sum(np.random.rand(100))
    a.append(x)


num_bins = 20
a, bins, patches = plt.hist(a, num_bins)
plt.xlabel('Sum of ten random numbers')
plt.ylabel('Number of sums')
plt.title('Histogram of sums')
# expected value should be equal to 50
plt.show()
