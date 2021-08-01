# Author: Viktor Mamontov
# Convert a list of classes from a file into dictionary

my_keys = []
my_values = []

with open('list.txt') as my_file:
    for line in my_file:
        my_list = line.split(':')
        my_keys.append(my_list[0])
        my_values.append(my_list[1])

# count hours for all types of classes
k = 0
for i in my_values:
    for symbol in i:
        if symbol == '(':
            i = i.replace('(', ' ')
            numbers = [int(word) for word in i.split() if word.isdigit()]
            my_values[k] = sum(numbers)
    k += 1

# create new dictionary
zip_iterator = zip(my_keys, my_values)
my_dict = dict(zip_iterator)
print(my_dict)
