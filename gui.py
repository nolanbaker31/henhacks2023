import tkinter as tk
import tkinter.messagebox
import customtkinter as ct
from PIL import Image    #Pillow

import os
import random
import time
import glob


#System settings
ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Home(ct.CTk):
    
    def __init__(self,questionCount):
        super().__init__()
        self.count = 0

        self.curQ = 1
        self.curT = 0
        self.curG = 1
        self.curP = 1

        self.pgL = 0
        self.pgG = 0
        self.pgP = 0

        self.dirQ = os.path.dirname(os.path.abspath(__file__))+ '/questions'
        self.dirT = os.path.dirname(os.path.abspath(__file__)) + '/tutorial'

        self.seen_questions = []
        self.seen_questionsG = []
        self.seen_questionsP = []

        self.score = 0
        self.ans1 = "A"
        self.ans2 = "B"
        self.ans3 = "C"
        self.ans4 = "D"
        self.hint = ""

        self.qlen = len(glob.glob1(self.dirQ + '/bash',"*.txt"))
        self.glen = len(glob.glob1(self.dirQ + '/git',"*.txt"))
        self.plen = len(glob.glob1(self.dirQ + '/powershell',"*.txt"))


        #Making the GUI

        # configure window
        self.title("Command Quest")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
         
        #Side Bar for options
        self.sidebar_frame = ct.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1) 

        self.logo_label = ct.CTkLabel(self.sidebar_frame, text="Tabs", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ct.CTkButton(self.sidebar_frame, text = "About Us", command=self.intro)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ct.CTkButton(self.sidebar_frame, text = "Tutorial", command=self.explination)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ct.CTkButton(self.sidebar_frame, text = "Bash Questions", command=self.questions)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = ct.CTkButton(self.sidebar_frame, text = "Git Questions", command=self.git)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = ct.CTkButton(self.sidebar_frame, text = "Make Questions", command=self.powershell)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)

        self.build_intro()

    # Side Bar functions
    def intro(self):
        self.delete(self.count)
        self.count = 0
        self.build_intro()
        return
    def explination(self):
        self.delete(self.count)
        self.count = 1
        self.build_explination()
        return
    def questions(self):
        self.delete(self.count)
        self.count = 2
        self.build_questions()
        return
    def git(self):
        self.delete(self.count)
        self.count = 3
        self.build_git()
        return
    
    def powershell(self):
        self.delete(self.count)
        self.count = 4
        self.build_power()
    

    # Build functions
    def build_intro(self):
        #Function that builds the main entry front page
        self.textbox = ct.CTkTextbox(self, width=250, height = 350)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #Input for Text box
        intro = open("Intro.txt", 'r')
        self.textbox.insert("0.0",intro.read())
        self.textbox.configure(state = tk.DISABLED)
        return
    
    def build_explination(self):
        self.textbox = ct.CTkTextbox(self, width=600, height = 450, fg_color = "transparent")
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","") #Add to point towards intro
        self.textbox.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 250, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(5,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Navigation", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.tut_fwd)
        self.fwd.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.tut_back)
        self.back.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)

        return
     
    def build_questions(self):
        self.textbox = ct.CTkTextbox(self, width=600, height = 350)
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","") #Add to point towards an intro
        self.textbox.configure(state = tk.DISABLED)

        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0","") #Add to point towards an intro
        self.ansText.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 350, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(7,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Options", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.ans1 = ct.CTkButton(master=self.btn_frame, text = self.ans1, command= self.answer1L)
        self.ans1.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans2 = ct.CTkButton(master=self.btn_frame, text = self.ans2, command= self.answer2L)
        self.ans2.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans3 = ct.CTkButton(master=self.btn_frame, text = self.ans3, command= self.answer3L)
        self.ans3.grid(row = 3, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans4 = ct.CTkButton(master=self.btn_frame, text = self.ans4, command= self.answer4L)
        self.ans4.grid(row = 4, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.q_fwd)
        self.fwd.grid(row = 5, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.q_back)
        self.back.grid(row = 6, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        return 
    
    def build_git(self):
        self.textbox = ct.CTkTextbox(self, width=600, height = 350)
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","") #Add to point towards an intro
        self.textbox.configure(state = tk.DISABLED)

        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0","") #Add to point towards an intro
        self.ansText.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 350, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(7,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Options", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.ans1 = ct.CTkButton(master=self.btn_frame, text = self.ans1, command= self.answer1G)
        self.ans1.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans2 = ct.CTkButton(master=self.btn_frame, text = self.ans2, command= self.answer2G)
        self.ans2.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans3 = ct.CTkButton(master=self.btn_frame, text = self.ans3, command= self.answer3G)
        self.ans3.grid(row = 3, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans4 = ct.CTkButton(master=self.btn_frame, text = self.ans4, command= self.answer4G)
        self.ans4.grid(row = 4, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.g_fwd)
        self.fwd.grid(row = 5, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.g_back)
        self.back.grid(row = 6, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        return 
    
    def build_power(self):
        self.textbox = ct.CTkTextbox(self, width=600, height = 350)
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","") #Add to point towards an intro
        self.textbox.configure(state = tk.DISABLED)

        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0","") #Add to point towards an intro
        self.ansText.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 350, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(7,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Options", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.ans1 = ct.CTkButton(master=self.btn_frame, text = self.ans1, command= self.answer1P)
        self.ans1.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans2 = ct.CTkButton(master=self.btn_frame, text = self.ans2, command= self.answer2P)
        self.ans2.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans3 = ct.CTkButton(master=self.btn_frame, text = self.ans3, command= self.answer3P)
        self.ans3.grid(row = 3, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans4 = ct.CTkButton(master=self.btn_frame, text = self.ans4, command= self.answer4P)
        self.ans4.grid(row = 4, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.p_fwd)
        self.fwd.grid(row = 5, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.p_back)
        self.back.grid(row = 6, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        return 

    #Delete Function
    def delete(self,count):
        if(count == 0):
            self.del_intro()
            return
        elif(count == 1):
            self.del_explination()
            return
        elif(count == 2):
            self.del_questionsL()
            return
        elif(count == 3):
            self.del_git()
            return
        elif(count == 4):
            self.del_power()
    
    def del_intro(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()
        return
    def del_explination(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()

        self.btn_frame.destroy()
        return
    def del_questionsL(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()
        self.ansText.configure(state = tk.NORMAL)
        self.ansText.destroy()

        self.btn_frame.destroy()
        return
    def del_git(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()
        self.ansText.configure(state = tk.NORMAL)
        self.ansText.destroy()

        self.btn_frame.destroy()
        return
    def del_power(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()
        self.ansText.configure(state = tk.NORMAL)
        self.ansText.destroy()

        self.btn_frame.destroy()
        return

    #Button Functions
    
    

    
    #Tutorial Functions

    def tut_fwd(self):
        self.curT += 1
        f = open(self.dirT + '/prompts/intro' + str(self.curT) + '.txt', 'r')
        file_contents = f.read()
        f.close()
        self.del_explination()
        self.build_explination()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",file_contents)
        self.textbox.configure(state = tk.DISABLED)
        return

    def tut_back(self): # Function for button to move to last text document
        if self.curT == 1:
            return
        self.curT -= 1
        f = open(self.dirT + '/prompts/intro' + str(self.curT) + '.txt', 'r')
        file_contents = f.read()
        f.close()
        self.del_explination()
        self.build_explination()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",file_contents)
        self.textbox.configure(state = tk.DISABLED)
        return file_contents
    
    #Bash functions

    def q_fwd(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonL_next()
        self.del_questionsL()
        self.build_questions()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return
    def q_back(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonL_last()
        self.del_questionsL()
        self.build_questions()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return

    def choose_randomL(self,count): # Function for choosing a random, new question (no repeats)
        random.seed()
        if len(self.seen_questions) == count:
            return -1 # -1 means you have reached the end
        while True:
            question_num = random.randint(1, count)
            if question_num not in self.seen_questions:
                break
        self.seen_questions.append(question_num)
        return question_num

    def buttonL_next(self): # Function for button to move to next text document
        self.curQ = self.choose_randomL(self.qlen)
        f = open(self.dirQ + '/bash/question' + str(self.curQ) + '.txt', 'r')
        file_contents = f.read()
        f.close()

        f = open(self.dirQ + '/..' + '/answers/bash/answer' + str(self.curQ) + '.txt', 'r')
        file_content = f.read()
        answers = file_content.split(':')
        f.close()
        return file_contents, answers[1], answers[5], answers[9], answers[13] #Letter Answer Letter Answer
    
    def buttonL_submit(self,chosen_answer): # Function for choosing the answer to a question, returns explanation for chosen answer
        answer_map = {'A': 2, 'B': 6, 'C': 10, 'D': 14}
        f = open(self.dirQ + '/..' '/answers/bash/answer' + str(self.curQ) + '.txt', 'r')
        file_contents = f.read()
        answers = file_contents.split(':')
        if answers[answer_map[chosen_answer]] == '1':
            self.score+= 1
        f.close()
        return answers[answer_map[chosen_answer] + 1]
    
    def buttonL_last(self): # Function for button to move to last text document
        if self.seen_questions.index(self.curQ) == 0:
            return
        else:
            f = open(self.dirQ + '/bash/question' + str(self.seen_questions[self.seen_questions.index(self.curQ)-1]) + '.txt', 'r')
            file_contents = f.read()
            f.close()

            f = open(self.dirQ + '/..' + '/answers/bash/answer' + str(self.curQ) + '.txt', 'r')
            file_content = f.read()
            answers = file_content.split(':')
            f.close()
            return file_contents, answers[1], answers[5], answers[9], answers[13]

    def answer1L(self):
        text = self.buttonL_submit('A')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return 
    def answer2L(self):
        text = self.buttonL_submit('B')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer3L(self):
        text = self.buttonL_submit('C')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer4L(self):
        text = self.buttonL_submit('D')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    

    #Git Functions     
    

    def g_fwd(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonG_next()
        self.del_git()
        self.build_git()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return
    def g_back(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonG_last()
        print(self.buttonG_last())
        self.del_git()
        self.build_git()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return

    def choose_randomG(self,count): # Function for choosing a random, new question (no repeats)
        random.seed()
        if len(self.seen_questionsG) == count:
            return -1 # -1 means you have reached the end
        while True:
            question_num = random.randint(1, count)
            if question_num not in self.seen_questionsG:
                break
        self.seen_questionsG.append(question_num)
        return question_num

    def buttonG_next(self): # Function for button to move to next text document
        self.curG = self.choose_randomL(self.glen)
        f = open(self.dirQ + '/git/question' + str(self.curG) + '.txt', 'r')
        file_contents = f.read()
        f.close()

        f = open(self.dirQ + '/..' + '/answers/git/answer' + str(self.curG) + '.txt', 'r')
        file_content = f.read()
        answers = file_content.split(':')
        f.close()
        return file_contents, answers[1], answers[5], answers[9], answers[13] #Letter Answer Letter Answer
    
    def buttonG_submit(self,chosen_answer): # Function for choosing the answer to a question, returns explanation for chosen answer
        answer_map = {'A': 2, 'B': 6, 'C': 10, 'D': 14}
        f = open(self.dirQ + '/..' '/answers/git/answer' + str(self.curG) + '.txt', 'r')
        file_contents = f.read()
        answers = file_contents.split(':')
        if answers[answer_map[chosen_answer]] == '1':
            self.score+= 1
        f.close()
        return answers[answer_map[chosen_answer] + 1]
    
    def buttonG_last(self): # Function for button to move to last text document
        if self.seen_questionsG.index(self.curG) == 0:
            return
        else:
            f = open(self.dirQ + 'git/question' + str(self.seen_questionsG[self.seen_questionsG.index(self.curG)-1]) + '.txt', 'r')
            file_contents = f.read()
            f.close()

            f = open(self.dirQ + '/..' + '/answers/git/answer' + str(self.curG) + '.txt', 'r')
            file_content = f.read()
            answers = file_content.split(':')
            f.close()
            return file_contents, answers[1], answers[5], answers[9], answers[13]

    def answer1G(self):
        text = self.buttonG_submit('A')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return 
    def answer2G(self):
        text = self.buttonG_submit('B')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer3G(self):
        text = self.buttonG_submit('C')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer4G(self):
        text = self.buttonG_submit('D')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    

    #Git Functions     

    def p_fwd(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonP_next()
        self.del_power()
        self.build_power()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return
    def p_back(self):
        text, self.ans1, self.ans2, self.ans3, self.ans4 = self.buttonP_last()
        self.del_power()
        self.build_power()
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state = tk.DISABLED)
        return

    def choose_randomP(self,count): # Function for choosing a random, new question (no repeats)
        random.seed()
        if len(self.seen_questionsP) == count:
            return -1 # -1 means you have reached the end
        while True:
            question_num = random.randint(1, count)
            if question_num not in self.seen_questionsP:
                break
        self.seen_questionsG.append(question_num)
        return question_num

    def buttonP_next(self): # Function for button to move to next text document
        self.curP = self.choose_randomL(self.plen)
        f = open(self.dirQ + '/make/question' + str(self.curP) + '.txt', 'r')
        file_contents = f.read()
        f.close()

        f = open(self.dirQ + '/..' + '/answers/make/answer' + str(self.curP) + '.txt', 'r')
        file_content = f.read()
        answers = file_content.split(':')
        f.close()
        return file_contents, answers[1], answers[5], answers[9], answers[13] #Letter Answer Letter Answer
    
    def buttonP_submit(self,chosen_answer): # Function for choosing the answer to a question, returns explanation for chosen answer
        answer_map = {'A': 2, 'B': 6, 'C': 10, 'D': 14}
        f = open(self.dirQ + '/..' '/answers/make/answer' + str(self.curP) + '.txt', 'r')
        file_contents = f.read()
        answers = file_contents.split(':')
        if answers[answer_map[chosen_answer]] == '1':
            self.score+= 1
        f.close()
        return answers[answer_map[chosen_answer] + 1]
    
    def buttonP_last(self): # Function for button to move to last text document
        if self.seen_questionsG.index(self.curP) == 0:
            return
        else:
            f = open(self.dirQ + 'make/question' + str(self.seen_questionsG[self.seen_questionsP.index(self.curP)-1]) + '.txt', 'r')
            file_contents = f.read()
            f.close()

            f = open(self.dirQ + '/..' + '/answers/make/answer' + str(self.curP) + '.txt', 'r')
            file_content = f.read()
            answers = file_content.split(':')
            f.close()
            return file_contents, answers[1], answers[5], answers[9], answers[13]

    def answer1P(self):
        text = self.buttonP_submit('A')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return 
    def answer2P(self):
        text = self.buttonP_submit('B')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer3P(self):
        text = self.buttonP_submit('C')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return
    def answer4P(self):
        text = self.buttonP_submit('D')
        self.ansText.configure(state = tk.NORMAL)
        self.ansText = ct.CTkTextbox(self, width = 500, height = 100, fg_color= "transparent")
        self.ansText.grid(row = 4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.ansText.insert("0.0",text) #Add to point towards question 1
        self.ansText.configure(state = tk.DISABLED)

        return



if __name__ == "__main__":
    app = Home(0)
    app.mainloop()
