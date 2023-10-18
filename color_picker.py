from tkinter import *
from tkinter import colorchooser


def get_color():
    selected_color = colorchooser.askcolor(title="Select a color")
    print(selected_color)


window = Tk()
button = Button(window, text="Click me", command=get_color)
button.pack()
window.geometry("500x500")
window.mainloop()