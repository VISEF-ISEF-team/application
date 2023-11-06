import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
    
        # menu
        self.menu = Menu(self)
        self.mainframe = MainFrame(self)
        # self.entry = Entry(self, "entry", "submit", "black")
        # run
        self.mainloop()
        
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
        self.create_widgets()
        self.create_layouts()
        
    def create_widgets(self):
        self.menu_button1 = ttk.Button(self, text = 'Button 1')
        self.menu_button2 = ttk.Button(self, text = 'Button 2')
        self.menu_button3 = ttk.Button(self, text = 'Button 3')

        self.menu_slider1 = ttk.Scale(self, orient = 'vertical')
        self.menu_slider2 = ttk.Scale(self, orient = 'vertical')

        self.toggle_frame = ttk.Frame(self)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text = 'check 1')
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text = 'check 2')
        
        self.entry = ttk.Entry(self)
        
    def create_layouts(self):
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        self.menu_button1.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2, padx = 4, pady = 4)
        self.menu_button2.grid(row = 0, column = 2, sticky = 'nswe', padx = 4, pady = 4)
        self.menu_button3.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 4, pady = 4)

        self.menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = 'nsew', pady = 20)
        self.menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = 'nsew', pady = 20)

        # toggle layout
        self.toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
        self.menu_toggle1.pack(side = 'left', expand = True)
        self.menu_toggle2.pack(side = 'left', expand = True)
        
class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
        self.create_widgets()
        self.create_layout()
        
    def create_widgets(self):
        self.entry_frame1 = ttk.Frame(self)
        self.main_label1 = ttk.Label(self.entry_frame1, text = 'label 1', background = 'red')
        self.main_button1 = ttk.Button(self.entry_frame1, text = 'Button 1')

        self.entry_frame2 = ttk.Frame(self)
        self.main_label2 = ttk.Label(self.entry_frame2, text = 'label 2', background = 'blue')
        self.main_button2 = ttk.Button(self.entry_frame2, text = 'Button 2')


    def create_layout(self):
        self.entry_frame1.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.entry_frame2.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)

        self.main_label1.pack(expand = True, fill = 'both')
        self.main_button1.pack(expand = True, fill = 'both', pady = 10)

        self.main_label2.pack(expand = True, fill = 'both')
        self.main_button2.pack(expand = True, fill = 'both', pady = 10)


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)
        self.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.create_widgets(label_text, label_background, button_text)
        self.create_layouts()
        
    def create_widgets(self, label_text, label_background, button_text):
        self.label = ttk.Label(self, text = label_text, background = label_background)
        self.button = ttk.Button(self, text = button_text)

    def create_layouts(self):
        self.label.pack(expand = True, fill = 'both')
        self.button.pack(expand = True, fill = 'both', pady = 10)


app = MainApp(
    'VasculAR software',
    (600, 600)
)




# menu widgets
# menu_button1 = ttk.Button(menu_frame, text = 'Button 1')
# menu_button2 = ttk.Button(menu_frame, text = 'Button 2')
# menu_button3 = ttk.Button(menu_frame, text = 'Button 3')

# menu_slider1 = ttk.Scale(menu_frame, orient = 'vertical')
# menu_slider2 = ttk.Scale(menu_frame, orient = 'vertical')

# toggle_frame = ttk.Frame(menu_frame)
# menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'check 1')
# menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'check 2')

# entry = ttk.Entry(menu_frame)

# # menu layout
# menu_frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
# menu_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

# menu_button1.grid(row = 0, column = 0, sticky = 'nswe', columnspan = 2, padx = 4, pady = 4)
# menu_button2.grid(row = 0, column = 2, sticky = 'nswe', padx = 4, pady = 4)
# menu_button3.grid(row = 1, column = 0, columnspan = 3, sticky = 'nsew', padx = 4, pady = 4)

# menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = 'nsew', pady = 20)
# menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = 'nsew', pady = 20)

# # toggle layout
# toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
# menu_toggle1.pack(side = 'left', expand = True)
# menu_toggle2.pack(side = 'left', expand = True)

# # entry layout
# entry.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')

# # main widgets 
# entry_frame1 = ttk.Frame(main_frame)
# main_label1 = ttk.Label(entry_frame1, text = 'label 1', background = 'red')
# main_button1 = ttk.Button(entry_frame1, text = 'Button 1')

# entry_frame2 = ttk.Frame(main_frame)
# main_label2 = ttk.Label(entry_frame2, text = 'label 2', background = 'blue')
# main_button2 = ttk.Button(entry_frame2, text = 'Button 2')

# # main layout
# entry_frame1.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
# entry_frame2.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)

# main_label1.pack(expand = True, fill = 'both')
# main_button1.pack(expand = True, fill = 'both', pady = 10)

# main_label2.pack(expand = True, fill = 'both')
# main_button2.pack(expand = True, fill = 'both', pady = 10)
