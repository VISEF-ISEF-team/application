import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')


def display_description():
    description.configure(text="Diseases description")
    
def submit():
    description.configure(text=f"Description updated: {input.get()}")
    input.configure(state="disabled")
    
def clear():
    input.configure(state="normal")
    input.delete(0,len(description.cget("text")))
    
def checkbox_function():
    if check_var.get() == "on":
        description.configure(text="You checked the check box")
    else:
        description.configure(text="You did not checked the check box")   
        
def clear_all_options():
    checkbox.deselect()
    checkbox_2.deselect()

# button = customtkinter.CTkButton(app, text="my button", command=display_description)
# button.pack(padx=100, pady=80)

description = customtkinter.CTkLabel(app, text="")
description.pack(padx=100, pady=100)

# input = customtkinter.CTkEntry(app, width=200, placeholder_text="Enter your analysis and diagnosis:")
# input.pack(padx=100, pady=30)

# submit_button = customtkinter.CTkButton(app, text="Submit", command=submit)
# submit_button.pack(padx=80, pady=50)

# clear_button = customtkinter.CTkButton(app, text="Clear", command=clear)
# clear_button.pack(padx=100, pady=50)

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(app, text="Click here to agree with terms and conditions", variable=check_var, onvalue="on", offvalue="off", command=checkbox_function)
checkbox.pack(padx=100, pady=100)

check_var_2 = customtkinter.StringVar(value="on")
checkbox_2 = customtkinter.CTkCheckBox(app, text="Brightness", 
                                            variable=check_var_2, 
                                            onvalue="on", 
                                            offvalue="off",
                                            corner_radius=50)
checkbox_2.pack(padx=100, pady=98)

btn_clear_all_options = customtkinter.CTkButton(app, text="Clear all options", command=clear_all_options)
btn_clear_all_options.pack(padx=100, pady=50)

app.mainloop()
