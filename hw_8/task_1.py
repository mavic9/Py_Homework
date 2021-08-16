# Author: Victor Mamontov
# Make class for transformation of data format

class Data:
    def __init__(self, my_data):
        self.my_data = my_data

    @classmethod
    def get_int(cls, my_data):
        my_list = my_data.split('-')
        int_list = []
        for i in my_list:
            int_list.append(int(i))
        return int_list

    @staticmethod
    def test_int(my_data):
        my_list = my_data.split('-')
        a = int(my_list[0])
        b = int(my_list[1])
        c = int(my_list[2])
        if b != 2:
            if b == 4 or b == 6 or b == 9 or b == 11:
                if 0 < a < 31:
                    if 0 < b < 13:
                        if 0 < c < 2100:
                            return print(f'The data {my_data} is correct!')
                        else:
                            return print(f'Tne year {c} is incorrect!!!')
                    else:
                        return print(f'The month {b} is incorrect!!!')
                else:
                    return print(f'The day {a} is incorrect!!!')
            else:
                if 0 < a < 32:
                    if 0 < b < 13:
                        if 0 < c < 2100:
                            return print(f'The data {my_data} is correct!')
                        else:
                            return print(f'Tne year {c} is incorrect!!!')
                    else:
                        return print(f'The month {b} is incorrect!!!')
                else:
                    return print(f'The day {a} is incorrect!!!')
        elif c % 4 == 0 and a < 30:
            return print(f'The data {my_data} is correct!')
        elif a < 29:
            return print(f'The data {my_data} is correct!')
        else:
            return print(f'The day {a} is incorrect!!!')


data_1 = '29-02-1990'
data_2 = '31-12-2000'
data_3 = '29-02-2000'
print(Data.get_int(data_1))
Data.test_int(data_1)
print(Data.get_int(data_2))
Data.test_int(data_2)
print(Data.get_int(data_3))
Data.test_int(data_3)
