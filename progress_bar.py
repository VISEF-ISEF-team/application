import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.title('VasculAR software')
app.geometry("1600x800")
app.iconbitmap('imgs/logo.ico')


def increase_contrast():
    contrast_progress_bar.step()
    
def slider_volume_show(value):
    text_show_volume.configure(text=round(value, 0))
    
def start_reconstruction():
    reconstruction_progress_bar.start() 
    
def cancel_reconstruction():
    reconstruction_progress_bar.stop()

contrast_progress_bar = customtkinter.CTkProgressBar(app, orientation="horizontal")
contrast_progress_bar.set(0)
contrast_progress_bar.pack(pady=20)

increase_btn = customtkinter.CTkButton(app, text="+", corner_radius=50, width=20, height=10, command=increase_contrast)
increase_btn.pack(padx=10, pady=21)


reconstruction_progress_bar = customtkinter.CTkProgressBar(app, orientation="horizontal")
reconstruction_progress_bar.set(0)
reconstruction_progress_bar.pack(pady=20)

reconstruction_btn = customtkinter.CTkButton(app, text="Automatic 3D reconstruction", command=start_reconstruction)
reconstruction_btn.pack(padx=10, pady=21)

cancel_reconstruction_btn = customtkinter.CTkButton(app, text="Cancel process", command=cancel_reconstruction)
cancel_reconstruction_btn.pack(padx=10, pady=21)

max_slice = 206
slider_volume = customtkinter.CTkSlider(app, from_=0, to=max_slice, command=slider_volume_show)
slider_volume.pack(pady=22)

text_show_volume = customtkinter.CTkLabel(app, text="")
text_show_volume.pack(pady=23)

app.mainloop()