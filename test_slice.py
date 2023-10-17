import SimpleITK as sitk
import numpy as np
import customtkinter as ctk
import customtkinter
from PIL import Image

# Load the .nii.gz file as a SimpleITK image
img = sitk.ReadImage("imgs/PAT001.nii.gz")
img_array = sitk.GetArrayFromImage(img)


# Create a CustomTkinter window
window = customtkinter.CTk()
window.title('VasculAR software')
window.geometry("1600x800")
window.iconbitmap('imgs/logo.ico')


canvas = ctk.CTkCanvas(window, width=240, height=240)
canvas.pack()

# Create a slider widget to control the slice index
slider = ctk.CTkSlider(window, min_value=0, max_value=img_array.shape[0]-1, value=0)
slider.pack()

# Define a function that updates the canvas with the selected slice image
def update_image(event):
    slice_index = int(slider.get())
    slice_image = img_array[slice_index]
    pil_image = Image.fromarray(slice_image)
    ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(240, 240))
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=ctk_image)

slider.bind("<ButtonRelease-1>", update_image)
