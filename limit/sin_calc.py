# def for sin calculation
import math

def calc_sin(a):
    n = math.pi/180
    taylor_serie = []
    k = 0
    for i in range(1,11,2):
        taylor_serie.append(((n**i)*(a**i)/math.factorial(i))*(-1)**k) # члены ряда Тейлора
        k += 1
    result = sum(taylor_serie)
    return result


print(calc_sin(1))
print(calc_sin(25))
print(calc_sin(30))
