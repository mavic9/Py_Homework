# Author: Viktor Mamontov
# Создание функции для деления чисел

def my_div():
    """
    :return division of two numbers
    """
    a = int(input("Введите делимое: "))
    b = int(input('Введите делитель: '))
    if b != 0:
        c = a / b
    else:
        c = 'Ошибка: деление на ноль!'
    return c


your_div = my_div()
print(your_div)
