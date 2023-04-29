# -- buttons.py -- 
# File which loads all variables


#libraries
import os
import random
import time
#variable declarations
cur_file = 1
directory = os.path.dirname(os.path.abspath(__file__))
file_count = 0

seen_questions = [] # structure is file number: True


for path in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, path)):
        file_count += 1


f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

def choose_random(): # Function for choosing a random, new question (no repeats)
    random.seed()
    while question_num:= random.randint(1, file_count) in seen_questions:
        pass
    seen_questions
    
    


    return

def button_next(): # Function for button to move to next text document
    global cur_file
    cur_file += 1
    f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    return
    

def button_last(): # Function for button to move to last text document
    global cur_file
    if cur_file == 1:
        return
    cur_file -= 1
    f = open(directory + '/prompts/intro' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    return

button_next()
