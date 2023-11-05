import customtkinter as ctk
from tkinter import filedialog
import requests
import json

# set the appearance and theme of customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# create a customtkinter window
app = ctk.CTk()
app.title("File Uploader")
app.geometry("400x200")

# create a label to show the selected file name
file_label = ctk.CTkLabel(app, text="No file selected")
file_label.grid(row=0, column=0, padx=10, pady=10)

# create a button to open the file chooser dialog
def choose_file():
    # use filedialog.askopenfilename to get the file name
    filename = filedialog.askopenfilename()
    # update the label with the file name
    file_label.configure(text=filename)

choose_button = ctk.CTkButton(app, text="Choose File", command=choose_file)
choose_button.grid(row=0, column=1, padx=10, pady=10)

# create a label to show the upload status
status_label = ctk.CTkLabel(app, text="Ready to upload")
status_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# create a button to upload the file
def upload_file():
    # get the file name from the label
    filename = file_label.cget("text")
    # check if the file name is valid
    if filename != "No file selected":
        # update the status label
        status_label.configure(text="Uploading...")
        # use requests.post to send the file to an API or server
        # replace the url with your own API or server endpoint
        url = "https://example.com/upload"
        # use files parameter to attach the file
        files = {"file": open(filename, "rb")}
        # send the request and get the response
        response = requests.post(url, files=files)
        # check if the response is successful
        if response.status_code == 200:
            # parse the response as json
            data = json.loads(response.text)
            # get the link or other information from the data
            # replace link with your own key name
            link = data["link"]
            # update the status label with the link or other information
            status_label.configure(text=f"Upload successful: {link}")
        else:
            # update the status label with an error message
            status_label.configure(text=f"Upload failed: {response.status_code}")
    else:
        # update the status label with a warning message
        status_label.configure(text="Please choose a file first")

upload_button = ctk.CTkButton(app, text="Upload File", command=upload_file)
upload_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# start the main loop of customtkinter
app.mainloop()
