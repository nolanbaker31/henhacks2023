# -- buttons.py -- 
# File which loads all variables --> used for command line functionality rather than gui

#libraries
import os
import random
import time
import glob

#variable declarations
cur_file = 1 # for starting at file 1 (change to 0 if we start with 0)
questions_directory = os.path.dirname(os.path.abspath(__file__)) + '/questions'
file_count = 0 # amount of txt files

seen_questions = [] # contains the NUMBER of each question that has been seen
file_count = len(glob.glob1(questions_directory,"*.txt"))

answer_map = {'A': 2, 'B': 6, 'C': 10, 'D': 14} # used to map answer to correct/incorrect in answer.txt files
chosen_answer = 0
score = 0 # used to keep track of score

f = open(questions_directory + '/question' + str(cur_file) + '.txt', 'r')
file_contents = f.read()
f.close()

def choose_random(): # Function for choosing a random, new question (no repeats)
    random.seed()
    if len(seen_questions) == file_count:
        return -1 # -1 means you have reached the end
    while True:
        question_num = random.randint(1, file_count)
        if question_num not in seen_questions:
            break
    seen_questions.append(question_num)
    return question_num

def button_next(): # Function for button to move to next text document
    global cur_file
    cur_file = choose_random()
    f = open(questions_directory + '/question' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    #print(seen_questions)
    #print(cur_file)
    f.close()
    return

def get_answers(): # Function to receive answers to display, returns: A, answer, B, answer, etc...
    #print(cur_file)
    f = open(questions_directory + '/..' + '/answers/answer' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    answers = file_contents.split(':')
    return answers[0], answers[1], answers[4], answers[5], answers[8], answers[9], answers[12], answers[13]

def button_submit(chosen_answer): # Function for choosing the answer to a question, returns explanation for chosen answer
    print("You chose: " + chosen_answer)
    f = open(questions_directory + '/..' '/answers/answer' + str(cur_file) + '.txt', 'r')
    file_contents = f.read()
    answers = file_contents.split(':')
    if answers[answer_map[chosen_answer]] == '1':
        score+= 1
    f.close()
    print(answers[answer_map[chosen_answer] + 1])
    return answers[answer_map[chosen_answer] + 1]

def button_last(): # Function for button to move to last text document
    global cur_file
    if seen_questions.index(cur_file) == 0:
        return
    else:
        cur_file = seen_questions.index(cur_file)-1
        f = open(questions_directory + '/question' + str(seen_questions[cur_file]) + '.txt', 'r')
        get_answers()
        file_contents = f.read()
        print(file_contents)
        f.close()
        return
    
button_next()
button_next()
get_answers()
button_submit('B')
button_last()
