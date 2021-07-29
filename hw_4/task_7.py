# Author: Viktor Mamontov
# Script for generator of factorials

def my_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


x = 10
for el in my_factorial(x):
    print(el)
