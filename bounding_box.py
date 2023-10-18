import customtkinter
from PIL import Image, ImageTk
from tkinter import Canvas

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(padx=10, pady=10, expand=True, fill="both")

my_canvas = Canvas(master=frame1, height=500, width=500, background='black')
my_canvas.pack()

img = Image.open("imgs/slice1.png")
resized_image = img.resize((500,500))
image = ImageTk.PhotoImage(resized_image)
my_image = my_canvas.create_image(0, 0, image=image, anchor="nw")
my_canvas.create_oval(100, 50, 200, 150, outline="red", width=3)



app.mainloop()
