# Author: Viktor Mamontov
# Write a list of firm's profit into json file

import json

revenue = []
firms = []

with open('revenue.txt') as my_file:
    for line in my_file:
        my_list = line.split(' ')
        firms.append(my_list[0])
        revenue.append(int(my_list[2]) - int(my_list[3]))

zip_iterator = zip(firms, revenue)
my_dict = dict(zip_iterator)

profit = [i for i in revenue if i > 0]
average_profit = {'Average_profit': round(sum(profit)/len(profit), 2)}

my_list = [my_dict, average_profit]
print(my_list)

with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f)
