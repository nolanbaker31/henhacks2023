import tkinter as tk
import tkinter.messagebox
import customtkinter as ct
from PIL import Image    #Pillow


#System settings
ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Home(ct.CTk):

    def __init__(self,count):
        super().__init__()
        self.count = 0

        #Making the GUI

        # configure window
        self.title("Linux Helper")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2,3), weight=1)

        #self.build_text()
         
        #Side Bar for options
        self.sidebar_frame = ct.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1) 

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

    # Side Bar functions
    def intro(self):
        self.count = 0
        self.delete(self.count)
        self.build_intro()
        return
    def explination(self):
        self.count = 1
        self.delete(self.count)
        self.build_explination()
        return
    def questions(self):
        self.count = 2
        self.delete(self.count)
        self.build_questions()
        return
    def hardMode(self):
        self.count = 3
        self.delete(self.count)
        self.build_hardMode()
        return
    

    # Build functions
    def build_intro(self):
        return
    def build_explination(self):
        return 
    def build_questions(self):
        return 
    def build_hardMode(self):
        return 
    
    #Delete Function
    def delete(self,count):
        if(count == 0):
            return
        elif(count == 1):
            return
        elif(count == 2):
            return
        elif(count == 3):
            return



if __name__ == "__main__":
    app = Home(0)
    app.mainloop()
