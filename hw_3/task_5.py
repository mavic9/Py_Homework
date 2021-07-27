# Author: Viktor Mamontov
# Функция для возврата суммы вводимых чисел


def int_sum():
    b = []
    q = True

    while q:  # пока значение переменной True программа продолжает запрос ввода новых строк
        a = (list(input('Введите числа через пробел (или q для остановки программы): ').split(' ')))
        b += a
        k = 0
        while k < len(b):
            if b[k] != 'q':
                b[k] = float(b[k])
                k += 1
            else:
                q = False
                b.remove('q')
                b = b[:k]
        print(f'Сумма чисел - {sum(b)}')
    result = "The end of operations"
    return result


new_result = int_sum()
print(new_result)
