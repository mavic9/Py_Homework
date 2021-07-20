# Author: Victor Mamontov
# Вывод слов с новой строки с нумерацией и ограничением в 10 символов

a = input('Введите несколько слов через пробел: ').split(' ')

for n, i in enumerate(a, 1):
    print(f'{n} {i[:10]}')
