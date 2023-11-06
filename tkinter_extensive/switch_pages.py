import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
       
        self.option_bar = tk.Frame(self)
        self.option_bar.pack(pady=5)
        self.option_bar.pack_propagate(False)
        self.option_bar.configure(width=500, height=35)
        
        self.home_indicator = Indicator(self, 22)
        self.product_indicator = Indicator(self, 147)
        self.contact_indicator = Indicator(self, 272)
        self.about_indicator = Indicator(self, 397)
        
        self.home_btn = Button_bar(self, "Home", 0, self.home_indicator)
        self.product_btn = Button_bar(self, 'Product', 125, self.product_indicator)
        self.contact_btn = Button_bar(self, 'Contact', 250, self.contact_indicator)
        self.about_btn = Button_bar(self, 'About', 375, self.about_indicator)
        
          
        self.mainframe = MainFrame(self)
    

class Button_bar(tk.Button):
    def __init__(self, parent, text, x_pos, indicator):
        super().__init__(master=parent, text=text, font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: self.switch(parent=parent, indicator=indicator))
        self.place(x=x_pos, y=0, width=125)
        
    def switch(self, parent, indicator):
        for child in parent.winfo_children():
            if isinstance(child, tk.Label):
                child['bg'] = 'SystemButtonFace'
        indicator['bg'] = '#0097e8'
        
class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(fill='both', expand=True)
        
class Indicator(tk.Label):
    def __init__(self, parent, x_pos):
        super().__init__(master=parent)
        self.place(x=x_pos, y=30, width=80, height=2)
        
class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        
app = MainApp(
    'VasculAR software',
    (500, 500)
) 

app.mainloop()