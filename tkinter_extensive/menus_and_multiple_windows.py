import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
from table_and_treeview import DatabaseView
import ttkbootstrap as ttk


class MainApp(ttk.Window):
    def __init__(self):
        super().__init__(themename='solar')
        self.geometry('600x400')    
        
        # main menu
        self.menu = tk.Menu(self)

        # file menu
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label='Open nifti file', command=lambda: print('Open nifti file'))
        self.file_menu.add_command(label='Open dcm folder', command=lambda: print('Open dcm folder'))
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Close file', command=lambda: print('Close file'))
        self.menu.add_cascade(label='File', menu=self.file_menu)

        # file sub menu
        self.file_sub_menu_preferences = tk.Menu(self.menu, tearoff=False)
        self.file_sub_menu_preferences.add_command(label='Keyboard Shortcuts')
        self.file_sub_menu_preferences.add_command(label='Color themes')
        self.file_menu.add_cascade(label='preferences', menu=self.file_sub_menu_preferences)
        self.file_menu.add_command(label='Exit', command=self.destroy)

        # help menu
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.help_menu.add_command(label='Cloud database', command=lambda: print('Cloud database'))
        self.help_menu.add_command(label='Deep Learnining', command=lambda: print('Deep Learning'))
        self.menu.add_cascade(label='Help', menu=self.help_menu)

        # setting menu
        self.setting_menu = tk.Menu(self.menu, tearoff=False)
        self.setting_check = tk.StringVar()
        self.setting_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=self.setting_check)
        self.menu.add_cascade(label='Setting', menu=self.setting_menu)

        # setting sub menu
        self.setting_sub_menu_theme = tk.Menu(self.menu, tearoff=False)
        self.setting_sub_menu_theme.add_command(label='Dark')
        self.setting_sub_menu_theme.add_command(label='Light')
        self.setting_menu.add_cascade(label = 'theme', menu=self.setting_sub_menu_theme)

        self.setting_sub_menu_lang = tk.Menu(self.menu, tearoff=False)
        self.setting_sub_menu_lang.add_command(label='English')
        self.setting_sub_menu_lang.add_command(label='Vietnamese')
        self.setting_menu.add_cascade(label = 'language', menu=self.setting_sub_menu_lang)


        self.menu_btn = ttk.Menubutton(self, text='Menu Button')
        self.menu_btn.pack()
        self.button_sub_menu = tk.Menu(self.menu_btn, tearoff=False)
        self.button_sub_menu.add_command(label='Menu btn 1', command=lambda: print('test 1'))
        self.button_sub_menu.add_checkbutton(label = 'Check btn 1')
        self.menu_btn['menu'] = self.button_sub_menu
        self.configure(menu=self.menu)

        # Main content for multiple windows
        self.button1 = ttk.Button(self, text='open main window', command=self.create_new_win)
        self.button1.pack(expand=True)

        self.button2 = ttk.Button(self, text='close new window', command=self.close_window)
        self.button2.pack(expand=True)

        self.button3 = ttk.Button(self, text='messagebox window', command=self.message_box)
        self.button3.pack(expand=True)

    # messagebox + toplevel
    def message_box(self):
        answer = messagebox.askyesno('Confirmation', 'Are you sure to exit')
        if answer:
            self.destroy()

    def create_new_win(self):
        if not hasattr(self, 'new_win'):
            self.new_win = DatabaseView()
        else:
            self.new_win.lift()

    def close_window(self):
        if hasattr(self, 'new_win'):
            self.new_win.destroy()
            del self.new_win
        
app = MainApp()
app.mainloop()