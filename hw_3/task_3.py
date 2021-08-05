# Author: Viktor Mamontov
# Функция возвращает сумму наибольших двух аргументов из трех

def my_func(a, b, c):
    d = [a, b, c]
    d.sort()
    max_sum = d[1] + d[2]
    return print(max_sum)


n1 = int(input('Введите первое число: '))
n2 = int(input('Введите первое число: '))
n3 = int(input('Введите третье число: '))

my_func(n1, n2, n3)
