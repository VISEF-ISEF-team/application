import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

app = tk.Tk()
app.geometry('600x400')

# main menu
menu = tk.Menu(app)

# file menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='Open nifti file', command=lambda: print('Open nifti file'))
file_menu.add_command(label='Open dcm folder', command=lambda: print('Open dcm folder'))
file_menu.add_separator()
file_menu.add_command(label='Close file', command=lambda: print('Close file'))
menu.add_cascade(label='File', menu=file_menu)

# file sub menu
file_sub_menu_preferences = tk.Menu(menu, tearoff=False)
file_sub_menu_preferences.add_command(label='Keyboard Shortcuts')
file_sub_menu_preferences.add_command(labe='Color themes')
file_menu.add_cascade(label='preferences', menu=file_sub_menu_preferences)
file_menu.add_command(label='Exit', comman=app.destroy)

# help menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Cloud database', command=lambda: print('Cloud database'))
help_menu.add_command(label='Deep Learnining', command=lambda: print('Deep Learning'))
menu.add_cascade(label='Help', menu=help_menu)

# setting menu
setting_menu = tk.Menu(menu, tearoff=False)
setting_check = tk.StringVar()
setting_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=setting_check)
menu.add_cascade(label='Setting', menu=setting_menu)

# setting sub menu
setting_sub_menu_theme = tk.Menu(menu, tearoff=False)
setting_sub_menu_theme.add_command(label='Dark')
setting_sub_menu_theme.add_command(label='Light')
setting_menu.add_cascade(label = 'theme', menu=setting_sub_menu_theme)

setting_sub_menu_lang = tk.Menu(menu, tearoff=False)
setting_sub_menu_lang.add_command(label='English')
setting_sub_menu_lang.add_command(label='Vietnamese')
setting_menu.add_cascade(label = 'language', menu=setting_sub_menu_lang)


menu_btn = ttk.Menubutton(app, text='Menu Button')
menu_btn.pack()
button_sub_menu = tk.Menu(menu_btn, tearoff=False)
button_sub_menu.add_command(label='Menu btn 1', command=lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'Check btn 1')
# menu_btn.configure(menu = button_sub_menu)
menu_btn['menu'] = button_sub_menu

app.configure(menu=menu)
app.mainloop()