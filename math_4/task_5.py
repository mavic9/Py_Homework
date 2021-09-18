import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.7

x = np.random.rand(100)
y = x*r + (1-r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# regression via calculation
a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)**2 - n*np.sum(x**2))
b = (np.sum(y) - a*np.sum(x))/n

# find coefficients of regression via numpy
A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]

# the correlation coefficient
R = np.sum((x - np.mean(x))*(y - np.mean(y)))/np.sqrt((np.sum((x - np.mean(x))**2))*(np.sum((y - np.mean(y))**2)))

print(f'The correlation coefficirnt is equal to {R.round(4)}')
print(np.corrcoef(x, y).round(4))
print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])

plt.show()
