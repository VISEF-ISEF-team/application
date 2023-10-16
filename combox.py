import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')

def change_colormap(choice):
    output_label.configure(text=choice)

text = customtkinter.CTkLabel(app, text="Pick a color")
text.pack(pady=40)

colors = ["Spectrum", "Fire", "Hot-and-cold", "Gold", "Overlay", "Red Overlay", "Green overlay", "Blue overlay"]
default_combox = customtkinter.StringVar(value="Select colormap")
colors_selection = customtkinter.CTkComboBox(app, values=colors, command=change_colormap, variable=default_combox)
colors_selection.pack(pady=42)

output_label = customtkinter.CTkLabel(app, text="")
output_label.pack(pady=46)

app.mainloop()
