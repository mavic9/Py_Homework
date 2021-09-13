import numpy as np
import matplotlib.pyplot as plt


def solver(a: np.array, x0: float, xk: float) -> list:
    """the function works for positive branch of increasing hyperbole"""
    x = np.pi / a  # sin(X) = 0 if X = n*Pi for n belonging to Z
    min_x = min(x)  # find the minimum value of f(a) to test conditions
    x_array = []  # a list for saving solutions
    n = 1
    while n * min_x < xk:  # test function for n
        new_x = []
        for i in x:
            if xk > i > x0:  # an additional test of condition for common case of limitations
                new_i = i * n
                if new_i < xk:
                    new_x.append(new_i)
        x_array.append(new_x)
        n += 1
    return x_array


x0 = 100  # minimal x limit
xk = 500  # maximal x limit
a = np.linspace(0.01, 0.02, 100)
x = solver(a, x0, xk)

n = 1
for i in x:
    plt.plot(a[100 - len(i):], i, label=f'for n={n}')  # keep a compliance for array size
    plt.ylabel('x', fontsize=16)
    plt.xlabel('a', fontsize=16)
    plt.title('x(a) for sin(x/a)=0', fontsize=16)
    plt.legend(loc='upper left', frameon=False)
    n += 1
plt.show()
