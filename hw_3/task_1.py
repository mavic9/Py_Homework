# Author: Viktor Mamontov
# Создание функции для деления чисел

def my_div(a, b):
    """
    :return division of two numbers
    """
    if b != 0:
        c = a / b
    else:
        c = 'Ошибка: деление на ноль!'
    return c


a = int(input("Введите делимое: "))
b = int(input('Введите делитель: '))
your_div = my_div(a,b)
print(your_div)
