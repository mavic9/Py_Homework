# Author: Victor Mamontov
# Определние времени года по номеру месяца
# Решение через словарь со списком значений

a = int(input('Введите номер месяца: '))

seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

if 0 < a < 13:
    for key, value in seasons.items():
        for i in value:
            if i == a:
                print(f'Сезон года - {key}')
                break
else:
    print('Месяц введен некоректно!')
