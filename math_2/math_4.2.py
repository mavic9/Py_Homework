import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

x = np.linspace(-2, 5, 501)
y1 = (np.exp(x) + x - 1)/x
y2 = x**2 - 1
fig1 = plt.figure(1)
plt.plot(x, y1)
plt.plot(x, y2)
# plt.plot(x, np.sign(y1), linestyle = "dotted") # sign of f(x) > 0 but y1 should be less f(x)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 20)
plt.grid(True)
# show solution of the inequality y1 via blue filling
plt.fill_between(x,y1, -2,color='b',alpha=.2)
fig1.suptitle('y < f(x) for the system', fontsize=20)

# show solution of the system of inequalities
x1 = np.linspace(-1.58, 2.62, 101)
x2 = np.linspace(4.2, 5, 51)
fig2 = plt.figure(2)
plt.plot(x1, x1**2-1, linewidth = 2, color='red')
plt.plot(x2, x2**2-1, linewidth = 2, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 20)
plt.grid(True)
fig2.suptitle('The solution of the system', fontsize=20)

plt.show()
print(f'The solution of the system is f(x) = x^2-1 in a range of x at (-1.5818, 2.6181) and (4.2001, +INF)')
