import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')


tabview = customtkinter.CTkTabview(master=app, width=500, height=500)
tabview.pack(padx=100, pady=100)

tab_1 = tabview.add("axial")
tab_2 = tabview.add("sagittal")
tab_3 = tabview.add("coronal")

tabview.set("sagittal") 

button = customtkinter.CTkButton(tab_1)
button.pack(padx=20, pady=20)


app.mainloop()