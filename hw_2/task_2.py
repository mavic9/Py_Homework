# Author: Victor Mamontov
# Поменять в списке соседние элементы местами

a = list(input('Введите любую текстовую или числовую последовательность элементов через пробел: ').split(' '))
k = 0  # счетчик элементов в списке

while k < len(a) - 1:  # условие для непревышения индексов в списке
    a[k], a[k+1] = a[k+1], a[k]  # обмен значений через кортежи
    k += 2  # переход к следующим парным элементам
print(f'Обновленный список: {a}')
