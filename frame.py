import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

my_frame = customtkinter.CTkScrollableFrame(app, orientation="vertical", label_text="Choose one")
my_frame.pack(pady=10)

for i in range(20):
    customtkinter.CTkButton(my_frame, text="Click now").pack(pady=5)

app.mainloop()