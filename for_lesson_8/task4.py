import numpy as np
from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x**2-y**2+3*x*y**3-2*x**2*y**2+2*x-3*y-5, 3*y**3-2*x**2+2*x**3*y-5*x**2*y**2+5)

solv = dict()

for i in np.arange(-10, 10, 2):
    for j in np.arange(-10, 10, 2):
        (x, y), info, ier, mesg =  fsolve(equations, (i, j), full_output=True)
        if ier == 1:
            solv[round(x, 4)] = round(y, 4)

print(solv)
# output {-3.6531: -0.2748, 2.2178: 0.6102, 2.4944: 0.7083, 1.3757: -0.1748, 1.2733: 1.662}
