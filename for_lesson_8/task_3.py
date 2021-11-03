from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x**2-y**2+3*x*y**3-2*x**2*y**2+2*x-3*y-5, 3*y**3-2*x**2+2*x**3*y-5*x**2*y**2+5)

(x, y), info, ier, mesg = fsolve(equations, (3, 3), full_output=True)
print(round(x, 4), round(y, 4), ier)
