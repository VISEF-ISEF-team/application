import customtkinter

from tkinter import Canvas
from PIL import Image, ImageTk


def move(event):
    my_canvas.moveto(my_image,event.x-50,event.y-50)

def scan(event):
    my_canvas.scan_mark(event.x, event.y)

def drag(event):
    my_canvas.scan_dragto(event.x, event.y, gain=2)

def display_coords(event):
    my_label.configure(text=f"X: {event.x} Y:{event.y}")



app = customtkinter.CTk()
frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(padx=10,pady=10, expand=True, fill="both")

my_canvas = Canvas(master=frame1, height=100, width=100, bg="black")
my_canvas.pack(expand=True, fill="both")

#Resize image(originally 512 x 512)
img = Image.open("imgs/slice1.png")
resized_image = img.resize((100,100))
image = ImageTk.PhotoImage(resized_image)
frame1.image = image
my_image = my_canvas.create_image(0, 0, image=image, anchor="nw")
my_canvas.create_rectangle(100, 50, 200, 150, outline="red", width=3)


my_canvas.tag_bind(my_image,"<Button1-Motion>", move, add="+")
my_canvas.bind("<Button-3>", scan)
my_canvas.bind("<Button3-Motion>", drag)


#Provides X-Y coordinates of mouse cursor when canvas object is selected
my_label = customtkinter.CTkLabel(master=my_canvas, text="X: None Y: None")
my_label.pack(padx="10px", pady="10px", anchor="se")
my_canvas.tag_bind(my_image, "<Button1-Motion>", display_coords, add="+")


my_canvas.configure(scrollregion=my_canvas.bbox(my_image))


app.mainloop()