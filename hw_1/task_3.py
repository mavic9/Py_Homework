# Author: Victor Mamontov
# Найти сумму чисел n + nn + nnn, которые задал пользователь

n = int(input('Введите любое целое число от 1 до 9: '))

my_sum = n + 11*n + 111*n
print(f'Итоговая сумма: {my_sum}')

