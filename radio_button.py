import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_1.pack(pady=10)

radiobutton_2 = customtkinter.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_2.pack(pady=10)

app.mainloop()