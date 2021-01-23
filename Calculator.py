
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import compute
import math

class Calculator:
	def clear_entry(self, event=None):
		self.main_entry.delete(0, END)
		self.data = []
	
	def delete_command(self, event=None):
		self.main_entry.delete((len(self.strvar_entry.get())-1), END)
	
	def sum_shower(self):
		self.status = self.status_variable.get()
		summary = compute.ExpressionCalculator(self.data, self.status)
		self.sum = summary.main()
	
	def equal_command(self, event=None):
		self.setting_nums_and_signs()
		self.sum_shower()
		self.main_entry.insert(END, ("=" + str(self.sum)))
		self.sum = 0
	
	def setting_nums_and_signs(self):
		self.sign_list = []
		entry_val = self.strvar_entry.get()
		dcount = 0
		for digit in entry_val:
			dcount += 1
			if digit in self.numbers:
				self.number += digit
				if dcount == len(entry_val):
					self.data.append(self.number)
					self.number = ""
			else:
				if self.number != "":
					self.data.append(self.number)
					self.number = ""
				if digit in self.math_signs:
					self.math_sign = digit
					self.data.append(self.math_sign)
					self.math_sign = ""
				else:
					self.math_sign += digit
					for char in self.math_special_sign:
						if self.math_sign == char:
							self.data.append(self.math_sign)
							self.math_sign = ""
		count = 0
		for sign in self.data:
			count += 1
			float_num = None
			if sign == "π":
				self.data[count - 1] = math.pi
			if sign == "e":
				self.data[count - 1] = math.e
			try:
				float_num = float(sign)
				self.data[count - 1] = float_num
			except:
				continue
		print(self.data)
	
	def button_press(self, sign):
		self.main_entry.insert(END, sign)
		self.main_entry.xview("end")
	
	def __init__(self, root):
		root.title("Claculator")
		root.geometry("1060x552+175+0")
		root.resizable(width=False, height=False)
		root.config(bg="#343200")
		
		# setting variables and entries
		self.arial_font = ("Arial", "13")
		self.strvar_entry = StringVar(root, value="")
		self.status_variable = StringVar(root)
		self.numbers = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.math_signs = ['+', '-', '×', '÷', '^', '√', '(', ')', 'π', 'e']
		self.math_special_sign = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'Log', 'Exp']
		self.number = ""
		self.status = ""
		self.math_sign = ""
		self.data = []
		self.sum = 0
		
		self.frame = Frame(root)
		self.entry_scroll = Scrollbar(self.frame, orient=HORIZONTAL, bg="#000e5b", activebackground="#001483")
		self.main_entry = Entry(self.frame, textvariable=self.strvar_entry, font=self.arial_font, width=39, bd=15, bg="#012900", fg="#dde100", justify=RIGHT, xscrollcommand=self.entry_scroll.set)
		self.entry_scroll.config(command=self.main_entry.xview)
		self.entry_scroll.pack(side="bottom", fill="x")
		self.main_entry.pack(side="left", fill="x", expand=False, ipadx=5)
		self.frame.grid(row=0, column=0, columnspan=7, sticky=W)
		
		# Creating Buttons
		self.button_1 = Button(root, text="1", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("1"))
		self.button_2 = Button(root, text="2", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("2"))
		self.button_3 = Button(root, text="3", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("3"))
		self.button_4 = Button(root, text="4", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("4"))
		self.button_5 = Button(root, text="5", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("5"))
		self.button_6 = Button(root, text="6", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("6"))
		self.button_7 = Button(root, text="7", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("7"))
		self.button_8 = Button(root, text="8", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("8"))
		self.button_9 = Button(root, text="9", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("9"))
		self.button_0 = Button(root, text="0", font=self.arial_font, width=9, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("0"))
		self.button_dot = Button(root, text=".", font=self.arial_font, width=3, height=1, bd=5, bg="#4f4f4f", fg="#fcffbd", activebackground="#7c7c7c", activeforeground="#ff6e6e", command=lambda:self.button_press("."))
		self.equal_button = Button(root, text="=", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=self.equal_command)
		self.clear_button = Button(root, text="C", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=self.clear_entry)
		self.del_button = Button(root, text="DEL", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=self.delete_command)
		self.add_button = Button(root, text="+", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("+"))
		self.substr_button = Button(root, text="-", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("-"))
		self.multip_button = Button(root, text="×", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("×"))
		self.div_button = Button(root, text="÷", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("÷"))
		self.power_button = Button(root, text="^", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("^"))
		self.para_button_1 = Button(root, text="(", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("("))
		self.para_button_2 = Button(root, text=")", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press(")"))
		self.root_button = Button(root, text="√", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("√"))
		self.log_button = Button(root, text="Log", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("Log"))
		self.exp_button = Button(root, text="Exp", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("Exp("))
		self.change_box = ttk.Combobox(root, width=10, font=self.arial_font, state="readonly", justify="center", textvariable=self.status_variable)
		self.change_box["values"] = ("degree", "radian")
		self.change_box.current(0)
		self.sin_button = Button(root, text="sin", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("sin("))
		self.cos_button = Button(root, text="cos", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("cos("))
		self.tan_button = Button(root, text="tan", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("tan("))
		self.arcsin_button = Button(root, text="arcsin", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("arcsin("))
		self.arccos_button = Button(root, text="arccos", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("arccos("))
		self.arctan_button = Button(root, text="arctan", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("arctan("))
		self.pi_button = Button(root, text="π", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("π"))
		self.e_button = Button(root, text="e", font=self.arial_font, width=3, height=1, bd=5, bg="#23dce2", fg="#494500", activebackground="#23c3c9", activeforeground="#e8dd0b", command=lambda:self.button_press("e"))
		
		# placing buttons
		self.button_1.grid(row=4, column=0, sticky=W)
		self.button_2.grid(row=4, column=1, sticky=W)
		self.button_3.grid(row=4, column=2, sticky=W)
		self.button_4.grid(row=3, column=0, sticky=W)
		self.button_5.grid(row=3, column=1, sticky=W)
		self.button_6.grid(row=3, column=2, sticky=W)
		self.button_7.grid(row=2, column=0, sticky=W)
		self.button_8.grid(row=2, column=1, sticky=W)
		self.button_9.grid(row=2, column=2, sticky=W)
		self.button_0.grid(row=5, column=1, columnspan=2, sticky=W)
		self.button_dot.grid(row=5, column=0, sticky=W)
		self.para_button_1.grid(row=1, column=0, sticky=W)
		self.para_button_2.grid(row=1, column=1, sticky=W)
		self.del_button.grid(row=1, column=2, sticky=W)
		self.clear_button.grid(row=1, column=3, sticky=W)
		self.equal_button.grid(row=1, column=4, sticky=W)
		self.multip_button.grid(row=2, column=3, sticky=W)
		self.div_button.grid(row=3, column=3, sticky=W)
		self.substr_button.grid(row=4, column=3, sticky=W)
		self.add_button.grid(row=5, column=3, sticky=W)
		self.root_button.grid(row=2, column=4, sticky=W)
		self.power_button.grid(row=3, column=4, sticky=W)
		self.log_button.grid(row=5, column=4, sticky=W)
		self.exp_button.grid(row=4, column=4, sticky=W)
		self.change_box.grid(row=1, column=5, columnspan=6, sticky=W, ipadx=7, ipady=12)
		self.sin_button.grid(row=2, column=5 , sticky=W)
		self.cos_button.grid(row=3, column=5 , sticky=W)
		self.tan_button.grid(row=4, column=5 , sticky=W)
		self.arcsin_button.grid(row=2, column=6 , sticky=W)
		self.arccos_button.grid(row=3, column=6 , sticky=W)
		self.arctan_button.grid(row=4, column=6 , sticky=W)
		self.pi_button.grid(row=5, column=5, sticky=W)
		self.e_button.grid(row=5, column=6, sticky=W)
		
		

root = Tk()
Calculator(root)
root.mainloop()