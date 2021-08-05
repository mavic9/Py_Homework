# Author: Viktor Mamontov
# Функция для возведения числа в отрицательную степень (без использования оператора **)

def my_func(a, b):
    """
        :param a positive int or float
        :param b negative int
        :return negative exponent of a raised in the b-th
    """
    if b < 0:
        k = 1
        result = 1/a
        while k < abs(b):
            result = result/a
            k += 1
    else:
        result = 'Error: b should be negative!'
    return print(result)


n1 = float(input("Enter a real number: "))
n2 = int(input("Enter a negative integer: "))

my_func(a=n1, b=n2)
