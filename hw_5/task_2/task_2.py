# Author: Viktor Mamontov
# Script for counting of lines and words in txt file

def txt_count(filename):
    f = open(filename)
    line_count = 0
    world_count = 0
    for line in f:
        w = line.split(' ')
        world_count += len(w)
        line_count += 1
    return line_count, world_count


my_file = 'new_text.txt'
lines, words = txt_count(my_file)
print(f'Number of lines - {lines}, number of words - {words}.')
