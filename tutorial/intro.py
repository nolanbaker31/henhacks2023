# -- intro.py -- 
# File which loads all variables

import os

directory = os.path.dirname(os.path.abspath(__file__))

cur_file = 1

f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
def button_next(): # Function for button to move to next text document
    global cur_file
    cur_file += 1
    f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    

def button_last(): # Function for button to move to last text document
    global cur_file
    if cur_file == 1:
        return
    cur_file -= 1
    f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

button_next()
