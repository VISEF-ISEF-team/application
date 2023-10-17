import customtkinter as ctk
import tkinter as tk

# create the window
app = ctk.CTk()
app.title("Calculator")
app.geometry("300x300")

# create the entry widget to display the expression and result
entry = ctk.CTkEntry(app)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew") # place the entry on the first row and span four columns

# create a list of buttons with labels and commands
buttons = [
    ("7", lambda: entry.insert(tk.END, "7")), # insert 7 at the end of the entry
    ("8", lambda: entry.insert(tk.END, "8")), # insert 8 at the end of the entry
    ("9", lambda: entry.insert(tk.END, "9")), # insert 9 at the end of the entry
    ("+", lambda: entry.insert(tk.END, "+")), # insert + at the end of the entry
    ("4", lambda: entry.insert(tk.END, "4")), # insert 4 at the end of the entry
    ("5", lambda: entry.insert(tk.END, "5")), # insert 5 at the end of the entry
    ("6", lambda: entry.insert(tk.END, "6")), # insert 6 at the end of the entry
    ("-", lambda: entry.insert(tk.END, "-")), # insert - at the end of the entry
    ("1", lambda: entry.insert(tk.END, "1")), # insert 1 at the end of the entry
    ("2", lambda: entry.insert(tk.END, "2")), # insert 2 at the end of the entry
    ("3", lambda: entry.insert(tk.END, "3")), # insert 3 at the end of the entry
    ("*", lambda: entry.insert(tk.END, "*")), # insert * at the end of the entry
    (".", lambda: entry.insert(tk.END, ".")), # insert . at the end of the entry
    ("0", lambda: entry.insert(tk.END, "0")), # insert 0 at the end of the entry
    ("=", lambda: calculate()), # call calculate function when pressed
    ("/", lambda: entry.insert(tk.END, "/")), # insert / at the end of the entry
]

# create a function to evaluate and display the result
def calculate():
    try:
        result = eval(entry.get()) # evaluate the expression in the entry
        entry.delete(0, tk.END) # delete everything in the entry
        entry.insert(0, result) # insert the result in the entry
    except:
        entry.delete(0, tk.END) # delete everything in the entry
        entry.insert(0, "Error") # insert error message in the entry

# loop through the buttons list and create a CTkButton for each one
row = 1 # start from second row
column = 0 # start from first column
for label, command in buttons:
    button = ctk.CTkButton(app, text=label, command=command) # create a CTkButton with label and command
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew") # place the button on the grid with padding and sticky option
    column += 1 # increment column by one
    if column > 3: # if column is more than three
        column = 0 # reset column to zero
        row += 1 # increment row by one

# configure each row and column to have equal weight
for i in range(4):
    app.grid_rowconfigure(i, weight=1) 
    app.grid_columnconfigure(i, weight=1)

# start mainloop    
app.mainloop()
