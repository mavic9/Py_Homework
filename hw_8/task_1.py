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
        if 0 < int(my_list[0]) < 32:
            if 0 < int(my_list[1]) < 13:
                if 0 < int(my_list[2]) < 2100:
                    return print(f'The data {my_data} is correct!')
                else:
                    return print(f'Tne year {my_list[2]} is incorrect!!!')
            else:
                return print(f'The month {my_list[1]} is incorrect!!!')
        else:
            return print(f'The day {my_list[0]} is incorrect!!!')


data_1 = '10-12-1990'
data_2 = '31-14-2000'
print(Data.get_int(data_1))
Data.test_int(data_1)
print(Data.get_int(data_2))
Data.test_int(data_2)
