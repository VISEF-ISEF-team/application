import tkinter as tk
from tkinter import ttk
from random import choice

app = tk.Tk()
app.geometry('600x400')

# list
patient_names = ['Patient 1', 'Patient 2', 'Patient 3', 'Patient 4', 'Patient 5', 'Patient 6']
modalities = ['CT', "MRI", 'CT', "MRI", 'CT', "MRI"]
dates = ['2023/10/20', '2023/10/18', '2023/10/19', '2023/10/17', '2023/10/16', '2023/10/15']

# initialize table view
table = ttk.Treeview(app, columns= ('First', 'Second', 'Third'), show = 'headings')
table.heading('First', text='Patient name')
table.heading('Second', text='Modality')
table.heading('Third', text='Acquisition Date')
table.pack(fill='both', expand=True)

# insert value into table
table.insert(parent='', index=0, values= ('Patient 1', 'CT', '2023/10/20'))
for i in range(6):
    patient_name = choice(patient_names)
    modality = choice(modalities)
    date = choice(dates)
    data = (patient_name, modality, date)
    table.insert(parent='', index=0, values=data)
             
# items
def item_selection(_):
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        print(f'delete {table.item(i)["values"]}')
        table.delete(i)
    print('delete done')

# table binding
table.bind('<<TreeviewSelect>>', item_selection)
table.bind('<Delete>', delete_items)


app.mainloop()