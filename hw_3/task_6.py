# Author: Viktor Mamontov
# Функция для возврата слова с заглавной буквы

def int_func(a):
    a = a[0].upper() + a[1:].lower()
    return a


print(int_func('hello'))

new_phrase = input('Введите слова в нижнем регистре через пробел: ').split(' ')

for i in new_phrase:
    print(f'{int_func(i)}', end=' ')
