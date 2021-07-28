# Author: Victor Mamontov
# Структура Рейтинг с запросом новых элементов

my_list = [7, 6, 5, 5, 3]

a = int(input('Введите рейтинг нового элемента от 1 до 10: '))
k = 0

if 0 < a < 11:
    if a <= my_list[-1]:
        my_list.append(a)
        print(f'Новый рейтинг {my_list}')
    else:
        for i in my_list:
            while a <= my_list[k]:
                k += 1
        my_list.insert(k, a)
        print(f'Новый рейтинг {my_list}')
else:
    print('Некоректный ввод рейтинга!')
