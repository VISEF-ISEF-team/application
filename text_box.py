import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

def get_text():
    text = textbox.get("0.0", "end")
    print(text)

textbox = customtkinter.CTkTextbox(app)
textbox.pack(pady=10)

textbox.insert("0.0", "new text to insert")

btn = customtkinter.CTkButton(app, text='get text', command=get_text)
btn.pack(pady=10)

app.mainloop()