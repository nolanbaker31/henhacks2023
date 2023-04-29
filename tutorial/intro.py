# -- intro.py -- 
# File which loads all variables

import os

directory = os.path.dirname(os.path.abspath(__file__))

for files in os.listdir('prompts'):
    f = open(directory + '/prompts/' + files, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
