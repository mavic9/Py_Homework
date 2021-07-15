# Author: Victor Mamontov
# Поиск наибольшей цифры в заданном натуральном числе

n = int(input('Введите любое целое положительное число: '))
k = []

while n//10 > 0:
    k.append(n % 10)
    n = n // 10

k.append(n % 10)
print(f'Наибольшая цифра числа: {max(k)}')
