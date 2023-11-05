import customtkinter

from tkinter import Canvas
from PIL import Image, ImageTk


def move(event):
    my_canvas.moveto(my_image,event.x-50,event.y-50)

# def scan(event):
#     my_canvas.scan_mark(event.x, event.y)

# def drag(event):
#     my_canvas.scan_dragto(event.x, event.y, gain=2)



app = customtkinter.CTk()
frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(padx=10,pady=10, expand=True, fill="both")

my_canvas = Canvas(master=frame1, height=100, width=100, bg="black")
my_canvas.pack(expand=True, fill="both")

img = Image.open("imgs/slice1.png")
resized_image = img.resize((100,100))
image = ImageTk.PhotoImage(resized_image)
frame1.image = image

my_image = my_canvas.create_image(0, 0, image=image, anchor="nw")
my_canvas.tag_bind(my_image,"<Button1-Motion>", move, add="+")
my_canvas.configure(scrollregion=my_canvas.bbox(my_image))

app.mainloop()