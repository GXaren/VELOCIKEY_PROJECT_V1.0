import customtkinter as ctk #important importations at libraries
import random
import time
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

easy_mode = [
   "I am happy to see your face.",
    "The sun is bright and hot",
    "It is a cat",
    "She is nice.",
    "He can run fast.",
    "The sky is blue.",
    "They play games." 
]

medium_mode = [
    "The quick brown fox jumps over the lazy dog.",
    "A beautiful sunset painted the sky with vivid colors.",
    "In the heart of the city, people hurriedly go about their day.",
    "She enjoys playing the piano and composing her own music.",
    "The conference room was filled with professionals from diverse backgrounds.",
    "Navigating through a bustling market can be a challenging task.",
    "The ancient castle stands atop the hill, overlooking the village."
]

hard_mode = [
    "The intricacies of quantum mechanics continue to baffle 148 scientists.",
    "Navigating through a labyrinthine network of code is a developer's challenge.",
    "1942, Amidst the cacophony of a crowded city, finding inner peace is a quest.",
    "The symphony's crescendo *echoed* through the concert hall, leaving the audience in awe.",
    "Solving complex mathematical proofs, requires precision and dedication!.",
    "Mastering a foreign language involves grasping its nuances and idiomatic expressions.",
    "In the depths of the ocean, unknown species await discovery by intrepid explorers."
]

class GUI: #itong class ay gagawa ng buong working application
    def __init__(self):
        self.app = ctk.CTk() #magcrcreate ng window
        self.app.geometry("1280x920")
        self.app.title("Velocikey (1.0.0)")

        self.image_original= Image.open("C:/Users/Ace/Documents/VELOCIKEY_LOGO2.jpg") #mag iimport ng image from the file directory
        self.image_tk= ImageTk.PhotoImage(self.image_original)

        self.canvas = ctk.CTkCanvas(self.app, width=1100, height=300) #size of image(customtkinter or ctk.CTkCanvas)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.image_tk) #dito magpapakita(canvas.create_image) ang inimport mo na image, you can decide where to position the image.

        self.intro = ctk.CTkLabel(self.app,text="“A program that tests how fast the user inputs his types on the keyboard.”")#(customtkinter/ctk.CTkLabel) if u wanna add text widgets into the window
        self.intro.configure(font=("Times New Roman", 20))
        self.intro.pack(pady=30, padx=10)
        self.frame = ctk.CTkFrame(self.app, corner_radius=15,border_width=2)
        self.frame.pack(pady=10, padx=200, fill='both', expand=True)

        self.label = ctk.CTkLabel(self.frame, text='SELECT DIFFICULTY')#(customtkinter/ctk.CTkLabel) if u wanna add text widgets into the window
        self.label.configure(font=("Times New Roman", 30))
        self.label.pack(pady=80)

        self.user_entry = ctk.CTkEntry(self.frame, placeholder_text="    (easy, medium, or hard)", width=380, height=40)#(customtkinter/ctk.CTkEntry) making the user input entry widget kung saan magttype ng user ang difficulty niya
        self.user_entry.configure(font=("Times New Roman", 30))
        self.user_entry.pack( padx=10)

        self.button = ctk.CTkButton(self.frame, text='START TEST', command=self.start_typing_test, width=50, height=40,fg_color="#696969")#(customtkinter/ctk.CTkButton) making the button widget, yung function nya nasa "def start_typing_test()"
        self.button.configure(font=("Times New Roman", 20, "bold"))
        self.button.pack(pady=20, padx=10)

        self.result_label = ctk.CTkLabel(self.frame, text="")
        self.retry_button = ctk.CTkButton(self.frame, text='Retry', command=self.retry_test, width=50, height=40,fg_color="#696969")#(customtkinter/ctk.CTkButton) making the button widget, yung function nya nasa "def retry_test()"
        self.retry_button.configure(font=("Times New Roman", 20, "bold"))

        self.random_words = ""
        self.user_input_entry = ctk.CTkEntry(self.frame, placeholder_text="Type here", width=480, height=40)#(customtkinter/ctk.CTkEntry) making the user input entry widget kung saan magttype ng user ang mga literary pieces niya
        self.user_input_entry.configure(font=("Times New Roman", 15, "bold"))
        self.user_input_entry.pack_forget()
        self.user_input_entry.delete(0, 'end')
        self.user_input_entry.bind("<Return>", self.end_typing_test) #

        self.aaa = ctk.CTkLabel (self.app,text="Copyright © PYTHRONAUTS 2023. All Rights Reserved")#(customtkinter/ctk.CTkLabel) naglagay lang tayo ng copyright text sa baba para mas mukhang professional hahaha
        self.aaa.configure(font=("Times New Roman", 10 ))
        self.aaa.pack(pady=10)

        self.app.mainloop()#itong code ay mag iinitialize ng window
    
    def get_random_words(self, mode):#select difficulty at kukuha ng literary piece sa line #9
        random_number = random.randint(0, 6) #ung code na ito random magseselect sa anim na literary pieces
        if mode == "easy":
            return easy_mode[random_number]
        elif mode == "medium":
            return medium_mode[random_number]
        elif mode == "hard":
            return hard_mode[random_number]
        else:
            return "Invalid difficulty level"
    # wpm formula - ginawa ni will
    def words_per_minute(self, text, elapsed_time):
        word_count = len(text.split())
        wpm = (word_count / elapsed_time) * 60
        return wpm
    # accuracy formula - ginawa ni myke
    def word_accuracy(self, random_words, input_text):
        random_words_list = random_words.split()
        input_words = input_text.split()
        min_len = min(len(random_words_list), len(input_words))
        correct_count = sum(1 for r, i in zip(random_words_list[:min_len], input_words[:min_len]) if r == i)
        accuracy = (correct_count / len(random_words_list)) * 100
        return accuracy
    # event na mangayayari after napindot mo ung start test
    def start_typing_test(self):
        mode = self.user_entry.get().lower()
        if mode in ["easy", "medium", "hard"]:

            self.random_words = self.get_random_words(mode) #kukuha ng words based sa nainput na difficulty ng user doon sa def get_random_words() at ipapakita yun
            self.label.pack(pady=70)
            self.user_entry.pack(pady=1, padx=10)
            self.button.pack(pady=12, padx=10)
            self.result_label.pack(pady=12, padx=10)
            self.result_label.configure(text="", width=240, height=40)
            self.result_label.configure(font=("Times New Roman", 15, "bold"))   
            self.space = ctk.CTkLabel(self.app, text="") #naglagay lang ako ng ganito para maayos ko ung layout ng gui hehe wag nalang pansinin ito 
            self.space.configure(font=("Times New Roman", 30, "bold"))
            self.space.pack(pady=20)  
            self.user_entry.delete(0, 'end')
            self.user_entry.pack_forget()
            self.label.pack_forget()
            self.button.pack_forget()
            self.space.pack_forget() #aalisin ung mga previous widgets and such after ka nagpress ng start test button

            self.result_label.configure(text="Type the following:\n\n " + self.random_words, width=240, height=40) #itong code responsible siya sa "type the following tas yung mga literary piece"
            self.result_label.configure(font=("Times New Roman", 20, "bold"))
            self.user_input_entry.bind("<BackSpace>", lambda event: 'break')
            self.user_input_entry.pack(pady=1)
            self.result_label.pack(pady=70, padx=10)
            self.user_input_entry.configure(font=("Times New Roman", 15, "bold"))
            self.user_input_entry.focus() #sisiguraduhing magtytype na agad ung keyboard mo instead na ihhover mo pa ung mouse mo doon sa input type box.
            self.start_time = time.time() #magiimplement ang timer para sa pagcalculate ng wpm
        else:
             self.tryagain = ctk.CTk() # dito magpapakita ung window na nagsasabing invalid ung nainput mong difficulty
             self.tryagain.title("Velocikey (1.0.0)")
             self.tryagain.geometry("310x60")
             mode_label = ctk.CTkLabel(self.tryagain, text="Invalid difficulty, please try again.")
             mode_label.configure(font=("Times New Roman", 15,"bold"))
             mode_label.pack(pady=20)
             self.tryagain.mainloop()

# showing the wpm and accuracy - magbabase itong code sa def words_per_minute() at def word_accuracy() sa pagcalculate ng results
    def end_typing_test(self, event):
        ending_time = time.time()
        elapsed_time = ending_time - self.start_time
        user_input = self.user_input_entry.get()
        wpm = self.words_per_minute(user_input, elapsed_time)
        accuracy = self.word_accuracy(self.random_words, user_input)
        result_text = f"Words per minute: {wpm:.2f}\nWord accuracy: {accuracy:.2f}%"
        self.result_label.configure(text=result_text)
        self.retry_button.pack(pady=12, padx=10)
        self.user_input_entry.pack_forget()
# babalik ka uli sa una - dito gagana ung self.user_input_entry.bind("<Return>", self.end_typing_test) na code doon sa line 81
    def retry_test(self):
        self.retry_button.pack_forget()
        self.result_label.pack_forget()
        self.user_input_entry.pack_forget()

        self.label.pack(pady=70)
        self.user_entry.delete(0, 'end')
        self.user_input_entry.delete(0, 'end')
        self.user_entry.pack(pady=1, padx=10)
        self.button.pack(pady=12, padx=10)





if __name__ == "__main__":
    velocikey_raw_code = GUI() #itong code i believe to execute the whole program or code sa class GUI na ginawa natin