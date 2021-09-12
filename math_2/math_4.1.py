import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# hw_4.1
x = np.linspace(-2, 5, 201)
plt.plot(x, (np.exp(x) + x - 1)/x, color = 'steelblue')
plt.plot(x, x**2 - 1, color = 'orange')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 20)
plt.grid(True)
plt.show()

def equations(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x) + x*(1 - y) - 1)

x1, y1 = fsolve(equations, (-1.5, 1.5))
x2, y2 = fsolve(equations, (3, 6))
x3, y3 = fsolve(equations, (4, 17.5))
x4, y4 = fsolve(equations, (0, -1)) # for the 2nd Eq if x == 0 then y == all real numbers

# four points are the solutions for the system of equations
print(f'x1, y1 = ({x1.round(4)}, {y1.round(4)})')
print(f'x2, y2 = ({x2.round(4)}, {y2.round(4)})')
print(f'x3, y3 = ({x3.round(4)}, {y3.round(4)})')
# only for a form where x is not denominator
print(f'x4, y4 = ({x4.round(4)}, {y4.round(4)}) if x is not a denominator')
