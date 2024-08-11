import customtkinter as ctk
import random
import time

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1280x720")
app.title("test")

label = ctk.CTkLabel(app, text = "HELLOOOO")
label.configure(font=("Calibri", 30, "bold"))
label.pack(pady=100)

label1 = ctk.CTkLabel(app, text = "everyone")
label1.configure(font=("Calibri",30,"bold"))
label1.pack(pady=40)

def show_howareyou():
    label.pack_forget()
    label1.pack_forget()
    button.pack_forget()
    inputting()
    label2 = ctk.CTkLabel(app, text = "how are you")
    label2.configure(font=("Calibri", 30, "bold"))
    label2.pack(pady=12)

button = ctk.CTkButton(app, text = "click here", command=show_howareyou)
button.configure(font=("Calibri",30,"bold"))
button.pack(pady=1)

def inputting():
    user_entry = ctk.CTkEntry(app, width=400, height=40,)
    user_entry.configure(font=("Calibri",30))
    user_entry.pack(pady=2)

app.mainloop()

