import customtkinter as ctk
from random import choice

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos 
		self.end_pos = end_pos
		self.width = abs(start_pos - end_pos)

		# animation logic
		self.pos = self.end_pos
		self.in_start_pos = False

		# layout
		self.place(relx = self.end_pos, rely = 0, relwidth = self.width, relheight = 1)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos > self.end_pos:
			self.pos -= 0.01
			self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.01
			self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True

# exercise
# 1. animate the button and move it to the right side of the window
# 2. update the panel so it move in from the right

def move_btn():
	global button_x
	button_x += 0.001
	button.place(relx = button_x, rely = 0.5, anchor = 'center')
	
	if button_x < 0.9:
		window.after(10, move_btn)

	# configure 
	# colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
	# color = choice(colors)
	# button.configure(fg_color = color)

def infinite_print():
	global button_x
	button_x += 0.5
	if button_x < 10:
		print('infinite')
		print(button_x)
		window.after(100, infinite_print)

# window 
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# animated widget
animated_panel = SlidePanel(window, 0, -0.3)
ctk.CTkLabel(animated_panel, text = 'Label 1').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkLabel(animated_panel, text = 'Label 2').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkButton(animated_panel, text = 'Button', corner_radius = 0).pack(expand = True, fill = 'both', pady = 10)
ctk.CTkTextbox(animated_panel, fg_color = ('#dbdbdb','#2b2b2b')).pack(expand = True, fill = 'both', pady = 10)

# button
button_x = 0.5
button = ctk.CTkButton(window, text = 'toggle sidebar', command = animated_panel.animate)
button.place(relx = button_x, rely = 0.5, anchor = 'center')

# run
window.mainloop()