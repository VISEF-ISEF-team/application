# import tkinter module
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import tkinter

# create a root window
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('VasculAR software')
root.geometry("600x600")
root.iconbitmap('imgs/logo.ico')

# create a canvas widget
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# create a list to store the rectangle coordinates
rect_list = []

# define a function to handle mouse press event
def on_press(event):
    # store the mouse position as the start point of the rectangle
    global start_x, start_y
    start_x = event.x
    start_y = event.y

# define a function to handle mouse release event
def on_release(event):
    # get the mouse position as the end point of the rectangle
    end_x = event.x
    end_y = event.y

    # draw a rectangle on the canvas using the start and end points
    if radio_var.get() == 1:
        rect_id = canvas.create_rectangle(start_x, start_y, end_x, end_y, outline="red", width=3)
    else: 
        rect_id = canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=3)
        show_distance(start_x, start_y, end_x, end_y)

    # append the rectangle id and coordinates to the list
    rect_list.append((rect_id, start_x, start_y, end_x, end_y))

# define a function to redo the last rectangle
def redo():
    # check if the list is not empty
    if rect_list:
        # pop the last item from the list
        rect_id, _, _, _, _ = rect_list.pop()

        # delete the rectangle from the canvas
        canvas.delete(rect_id)

    
# define a function to clear all rectangles
def clear():
    # loop through the list and delete each rectangle from the canvas
    for rect_id, _, _, _, _ in rect_list:
        canvas.delete(rect_id)

    # clear the list
    rect_list.clear()
    line_distance.configure(text="")
    

# define a function to update the label with the mouse coordinates
def show_coords(event):
    # get the mouse position relative to the canvas
    x = event.x
    y = event.y

    # update the label text with the coordinates
    coordinate_label.configure(text=f"Coordinates: x={x}, y={y}")
    
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
    
def show_distance(start_x, start_y, end_x, end_y):
    euclidean_distance = ((end_x - start_x)**2 + (end_y - start_y)**2)**(1/2)
    line_distance.configure(text=f'Distance: {round(euclidean_distance,3)}')
    
    


img = Image.open("imgs/slice1.png")
resized_image = img.resize((500,500))
image = ImageTk.PhotoImage(resized_image)
my_image = canvas.create_image(0, 0, image=image, anchor="nw")

# create a button to clear all rectangles
clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack()

# create a button to redo the last rectangle
redo_button = customtkinter.CTkButton(root, text="Redo", command=redo)
redo_button.pack(pady=10)

# bind the functions to the mouse events on the canvas
canvas.bind("<Button-1>", on_press)
canvas.bind("<ButtonRelease-1>", on_release)

# bind the function to the motion event on the canvas
canvas.bind("<Motion>", show_coords)


radio_var = tkinter.IntVar(value=1)
Rectangle = customtkinter.CTkRadioButton(root, text="Rectangle",
                                             command=radiobutton_event, variable= radio_var, value=1)
line = customtkinter.CTkRadioButton(root, text="Line",
                                             command=radiobutton_event, variable= radio_var, value=2)

line_distance = customtkinter.CTkLabel(root, text="")
coordinate_label = customtkinter.CTkLabel(root, text="")


Rectangle.pack()
line.pack()
line_distance.pack()
coordinate_label.pack()

# start the main loop
root.mainloop()
