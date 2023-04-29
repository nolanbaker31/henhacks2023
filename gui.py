import tkinter as tk
import tkinter.messagebox
import customtkinter as ct
from PIL import Image    #Pillow

import os
import random
import time


#System settings
ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Home(ct.CTk):

    def __init__(self,count,question,explain):
        super().__init__()
        self.count = 0
        self.question = 0
        self.explain = 0

        #Making the GUI

        # configure window
        self.title("Linux Helper")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
         
        #Side Bar for options
        self.sidebar_frame = ct.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1) 

        self.logo_label = ct.CTkLabel(self.sidebar_frame, text="Tabs", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ct.CTkButton(self.sidebar_frame, text = "About Us", command=self.intro)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ct.CTkButton(self.sidebar_frame, text = "Explination", command=self.explination)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ct.CTkButton(self.sidebar_frame, text = "Questions", command=self.questions)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = ct.CTkButton(self.sidebar_frame, text = "Hard Mode", command=self.hardMode)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

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
    def hardMode(self):
        self.delete(self.count)
        self.count = 3
        self.build_hardMode()
        return
    

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
        self.textbox.insert("0.0","Hello") #Add to point towards intro
        self.textbox.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 250, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(5,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Navigation", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.e_fwd)
        self.fwd.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.e_back)
        self.back.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)


        return 
    def build_questions(self):
        self.textbox = ct.CTkTextbox(self, width=600, height = 450)
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","Question") #Add to point towards question 1
        self.textbox.configure(state = tk.DISABLED)

        self.btn_frame = ct.CTkFrame(self, width = 250, corner_radius=0)
        self.btn_frame.grid(row = 0, column = 4, rowspan = 4, sticky="nsew")
        self.btn_frame.grid_columnconfigure(0,weight=1)
        self.btn_frame.grid_rowconfigure(7,weight=1)

        self.logo_label = ct.CTkLabel(self.btn_frame, text="Options", font=ct.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.ans1 = ct.CTkButton(master=self.btn_frame, text = "Answer 1", command= self.answer1)
        self.ans1.grid(row = 1, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans2 = ct.CTkButton(master=self.btn_frame, text = "Answer 2", command= self.answer2)
        self.ans2.grid(row = 2, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans3 = ct.CTkButton(master=self.btn_frame, text = "Answer 3", command= self.answer3)
        self.ans3.grid(row = 3, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.ans4 = ct.CTkButton(master=self.btn_frame, text = "Answer 4", command= self.answer4)
        self.ans4.grid(row = 4, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)

        self.fwd = ct.CTkButton(master=self.btn_frame, text = "Next", command= self.e_fwd)
        self.fwd.grid(row = 5, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        self.back = ct.CTkButton(master=self.btn_frame, text = "Back", command=self.e_back)
        self.back.grid(row = 6, column = 0, rowspan = 1, sticky = "nsew", padx=20,pady=10)
        return 
    def build_hardMode(self):
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
            self.del_questions()
            return
        elif(count == 3):
            self.del_hardMode()
            return
    
    def del_intro(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()
        return
    def del_explination(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()

        self.btn_frame.destroy()
        return
    def del_questions(self):
        self.textbox.configure(state = tk.NORMAL)
        self.textbox.destroy()

        self.btn_frame.destroy()
        return
    def del_hardMode(self):
        return
    

    #Mid Button Functions
    #Need to add fuctions with parameters
    def e_fwd(self):
        self.tut_fwd()
        return
    def e_back(self):
        self.tut_back()
        return
    
    #Tutorial Functions

    def tut_fwd(self):
        return
    def tut_back(self):
        return
    
    #Question functions
    def answer1(self):
        return 
    def answer2(self):
        return
    def answer3(self):
        return
    def answer4(self):
        return


if __name__ == "__main__":
    app = Home(0,0,0)
    app.mainloop()


