# Author: Viktor Mamontov
# Script for writing of message in txt file

def file_gen(new_file):
    phrase = input("Enter your phrase: ")
    phrase_list = [phrase + '\n']
    my_stop = False
    with open(new_file, 'w') as new_obj:
        if phrase != '':
            while not my_stop:
                new_phrase = input('Enter your phrase (or press Enter to stop) : ')
                if new_phrase != '':
                    phrase_list.append(new_phrase + '\n')
                else:
                    my_stop = True
            new_obj.writelines(phrase_list)
        else:
            print('No message in your phrase!')
    print('New file is written!')
    return


file_name = input('Enter file name in format name.txt: ')
file_gen(file_name)
