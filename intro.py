# -- intro.py -- 
# File which loads all variables --> used for Command line functionality instead of GUI
import os

tutorial_directory = os.path.dirname(os.path.abspath(__file__)) + '/tutorial'

cur_file = 1

f = open(tutorial_directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
file_contents = f.read()
#print(file_contents)
f.close()
def button_next(): # Function for button to move to next text document
    global cur_file
    cur_file += 1
    f = open(tutorial_directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    print(file_contents)

def button_last(): # Function for button to move to last text document
    global cur_file
    if cur_file == 1:
        return
    cur_file -= 1
    f = open(tutorial_directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

button_next()
