import customtkinter

# window theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# window configuration
app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')
app.grid_columnconfigure((12), weight=1)

def button_callback():
    print("button pressed")
    
# column one
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")


# column two
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=2, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_3 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_3.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="w")
checkbox_4 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_4.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")

# column three
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=4, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_5 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_5.grid(row=1, column=4, padx=20, pady=(0, 20), sticky="w")
checkbox_6 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_6.grid(row=1, column=5, padx=20, pady=(0, 20), sticky="w")

# column four
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=6, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_5 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_5.grid(row=1, column=6, padx=20, pady=(0, 20), sticky="w")
checkbox_6 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_6.grid(row=1, column=7, padx=20, pady=(0, 20), sticky="w")

# column five
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=8, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_5 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_5.grid(row=1, column=8, padx=20, pady=(0, 20), sticky="w")
checkbox_6 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_6.grid(row=1, column=9, padx=20, pady=(0, 20), sticky="w")

# column six
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=10, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_5 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_5.grid(row=1, column=10, padx=20, pady=(0, 20), sticky="w")
checkbox_6 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_6.grid(row=1, column=11, padx=20, pady=(0, 20), sticky="w")


app.mainloop()