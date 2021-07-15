# Author: Victor Mamontov
# Конвертация секунд в формат чч:мм:сс
sec = int(input('Введите время в секундах целым числом: '))

hh = int(sec//3600)
mm = int((sec%3600)//60)
ss = int(sec%60)

if hh > 9:                          #условие для соблюдения формата вывода
    if mm > 9:
        if ss > 9:
            print(f'{hh}:{mm}:{ss}')
        else:
            print(f'{hh}:{mm}:0{ss}')
    else:
        if ss > 9:
            print(f'{hh}:0{mm}:{ss}')
        else:
            print(f'{hh}:0{mm}:0{ss}')
else:
    if mm > 9:
        if ss > 9:
            print(f'0{hh}:{mm}:{ss}')
        else:
            print(f'0{hh}:{mm}:0{ss}')
    else:
        if ss > 9:
            print(f'0{hh}:0{mm}:{ss}')
        else:
            print(f'0{hh}:0{mm}:0{ss}')
