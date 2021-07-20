# Author: Victor Mamontov
# Конвертация секунд в формат чч:мм:сс
sec = int(input('Введите время в секундах целым числом: '))

hh = int(sec//3600)
mm = int((sec%3600)//60)
ss = int(sec%60)

print(f'{hh:02}:{mm:02}:{ss:02}')
