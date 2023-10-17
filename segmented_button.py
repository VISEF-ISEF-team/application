import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')


def clicker(value):
    view_option.configure(text=f"{value} view choosed")

views = ['axial', 'sagittal', 'coronal']
my_seg_bton = customtkinter.CTkSegmentedButton(app, values=views, command=clicker)
my_seg_bton.pack(pady=10)
my_seg_bton.set('axial')

view_option = customtkinter.CTkLabel(app, text="")
view_option.pack(pady=10)
app.mainloop()