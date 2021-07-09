from tkinter import*

class Calculator(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.kroo = False
		self.pack()

		self.problem = Entry(self, width=53, borderwidth=0, justify="right", relief=RIDGE, fg="white", font=("arial", "11", "bold"), bg="#022954")
		self.problem.grid(row=0, column=0, columnspan=6, padx=15, pady=45)

	def solve(self):
		try:
			result = self.problem.get()
			resultfinal = eval(result)
		except:
			self.problem.delete(0, END)
			self.problem.insert(0, "Error")
		else:
			self.problem.delete(0, END)
			self.problem.insert(0, resultfinal)

		global kroo
		self.kroo = True
		return self.kroo

	def delonecharac(self):
		global kroo
		if self.kroo == True:
			self.kroo = False
		meow = self.problem.get()
		arf = len(meow)-1
		self.problem.delete(arf, END)


	def clearall(self):
		self.problem.delete(0, END)
	

	def click(self, enter):
		global kroo
		if self.kroo == True:
			self.kroo = False
		meow = self.problem.get()
		arf = meow + enter
		self.problem.delete(0, END)
		self.problem.insert(0, arf)
		return self.problem.get()


