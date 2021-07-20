# Author: Victor Mamontov
# Структура данных Товары и сбор аналитики
a = int(input('Введите число доступных товаров: '))
k = 1  # счетчик товаров
my_list = []

while k <= a:
    features = list(input(f'Введиете название, цену и количество товара №{k} через пробел: ').split(' '))
    goods = (k, {'название': str(features[0]), 'цена': int(features[1]), 'количество': int(features[2]), 'ед': 'шт.'})  # создание кортежа для хранения атрибутов товара
    my_list.append(goods)
    k += 1
print(my_list)  # вывод данных

my_data = {'название': [], 'цена': [], 'количество': [], 'ед': 'шт.'}  # создание словаря с пустыми значениями для аналитики

for i in my_list:
    new_dict = i[1]
    for key, value in new_dict.items():
        if key == 'ед':  # для соответствия ключа 'ед' одному значению 'шт.'
            continue
        else:
            my_data[key].append(value)  # добавление аналитики о товарах в словарь
print(my_data)  # вывод аналитики о товарах в виде словаря
