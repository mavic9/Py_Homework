# Author: Victor Mamontov
# Определние времени года по номеру месяца
# Решение через список (без словаря)

a = int(input('Введите номер месяца: '))

seasons = ['зима', 'весна', 'лето', 'осень']

if 0 < a < 13:
    if a == 1 or a == 2 or a == 12:
        print(f'Сезон года - {seasons[0]}')
    elif a == 3 or a == 4 or a == 5:
        print(f'Сезон года - {seasons[1]}')
    elif a == 6 or a == 7 or a == 8:
        print(f'Сезон года - {seasons[2]}')
    else:
        print(f'Сезон года - {seasons[3]}')
else:
    print('Месяц введен некоректно!')
