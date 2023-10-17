import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

scrollable_frame = customtkinter.CTkScrollableFrame(app, width=200, height=200)
scrollable_frame.pack(pady=10)
app.mainloop()
