import customtkinter as ctk
from CTkColorPicker import *

def ask_color():
    pick_color = AskColor() # open the color picker
    color = pick_color.get() # get the color string
    button.configure(fg_color=color)
    
root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.iconbitmap('imgs/logo.ico')

button = ctk.CTkButton(master=root, text="CHOOSE COLOR", text_color="white", command=ask_color)
button.pack(padx=30, pady=20)
root.mainloop()