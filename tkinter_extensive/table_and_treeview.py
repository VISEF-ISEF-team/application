import tkinter as tk
# from tkinter import ttk
from random import choice
import ttkbootstrap as ttk


class DatabaseView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        patient_names = ['Patient 1', 'Patient 2', 'Patient 3', 'Patient 4', 'Patient 5', 'Patient 6']
        modalities = ['CT', "MRI", 'CT', "MRI", 'CT', "MRI"]
        dates = ['2023/10/20', '2023/10/18', '2023/10/19', '2023/10/17', '2023/10/16', '2023/10/15']
        
        # initialize table view
        self.table = ttk.Treeview(self, columns= ('First', 'Second', 'Third'), show = 'headings')
        self.table.heading('First', text='Patient name')
        self.table.heading('Second', text='Modality')
        self.table.heading('Third', text='Acquisition Date')
        self.table.pack(fill='both', expand=True)

        # insert value into table
        self.table.insert(parent='', index=0, values= ('Patient 1', 'CT', '2023/10/20'))
        for i in range(6):
            patient_name = choice(patient_names)
            modality = choice(modalities)
            date = choice(dates)
            data = (patient_name, modality, date)
            self.table.insert(parent='', index=0, values=data)
                
        # table binding
        self.table.bind('<<TreeviewSelect>>', self.item_selection)
        self.table.bind('<Delete>', self.delete_items)

    # items
    def item_selection(self,_):
        for i in self.table.selection():
            print(self.table.item(i)['values'])

    def delete_items(self,_):
        for i in self.table.selection():
            print(f'delete {self.table.item(i)["values"]}')
            self.table.delete(i)
        print('delete done')

