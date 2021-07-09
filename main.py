from tkinter import*

class Calculator(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.calcgui()
		self.kroo = False
		self.pack()

	def solve(self):
		try:
			result = self.problem.get()
			resultfinal = eval(result)
		except:
			self.problem.delete(0, END)
			self.problem.insert(0 ,"Error")
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
		
	def calcgui(self):

		self.groupname = Label(self, text="Tetrapython Brigade Calculator", width=35,padx=0,pady=8, borderwidth=0, justify="right", relief=RIDGE, fg="#E0E1E4", font=("Impact", "18"),bg="#022954")
		self.groupname.place(relx = 1.0,rely = 0.0,anchor ='ne')

		self.problem = Entry(self, width=53, borderwidth=0, justify="right", relief=RIDGE, fg="white", font=("arial", "11", "bold"), bg="#022954")
		self.problem.grid(row=0, column=0, columnspan=6, padx=15, pady=45)

		onebutt = Button(self, text="1", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce", command= lambda:self.click("1"))
		onebutt.grid(row=3, column=0, padx=3, pady=3)
		
		twobutt = Button(self,text="2", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("2"))
		twobutt.grid(row=3, column=1, padx=3, pady=3)
		
		threebutt = Button(self, text="3", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("3"))
		threebutt.grid(row=3, column=2, padx=3, pady=3)
		
		fourbutt = Button(self,text="4", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("4"))
		fourbutt.grid(row=2, column=0, padx=3, pady=3)
		
		fivebutt = Button(self,text="5", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("5"))
		fivebutt.grid(row=2, column=1, padx=3, pady=3)
		
		sixbutt = Button(self,text="6", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("6"))
		sixbutt.grid(row=2, column=2, padx=3, pady=3)
		
		sevenbutt = Button(self,text="7", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("7"))
		sevenbutt.grid(row=1, column=0, padx=3, pady=3)
		
		eightbutt = Button(self,text="8", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("8"))
		eightbutt.grid(row=1, column=1, padx=3, pady=3)
		
		ninebutt = Button(self,text="9", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("9"))
		ninebutt.grid(row=1, column=2, padx=3, pady=3)
		
		zerobutt = Button(self,text="0", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("0"))
		zerobutt.grid(row=4, column=0, padx=3, pady=3)
		
		decimalbutt = Button(self,text=".", width=12, pady=15, fg="black",font=("Bebas", "9" ,"bold" ), bg="#b0b8ce",command= lambda:self.click("."))
		decimalbutt.grid(row=5, column=0, padx=3, pady=3) 
		
		plusbutt = Button(self,text="+",  width=20,pady=15, fg="White",font=("Arial", "9" ,"bold" ), bg="#505a74",command= lambda:self.click("+"))
		plusbutt.grid(row=1, column=3, padx=3, pady=3)
		
		minusbutt = Button(self,text="-",  width=20,pady=15, fg="White",font=("Arial", "9" ,"bold" ), bg="#505a74",command= lambda:self.click("-"))
		minusbutt.grid(row=2, column=3, padx=3, pady=3)
		
		timesbutt = Button(self,text="x", width=20,pady=15, fg="White",font=("Arial", "9" ,"bold" ), bg="#505a74",command= lambda:self.click("*"))
		timesbutt.grid(row=3, column=3, padx=3, pady=3)
		
		dividebutt = Button(self, text="÷", width=20, pady=15, fg="White", font=("Arial", "9" ,"bold" ), bg="#505a74", command=lambda: self.click("/"))
		dividebutt.grid(row=4, column=3, padx=3, pady=3)
		
		equalsbutt = Button(self, text="=", width=20, pady=15, fg="White",font=("Arial", "9" ,"bold" ), bg="#505a74",command= lambda:self.solve())
		equalsbutt.grid(row=5, column=3, padx=3, pady=3)
		
		clearbutt = Button(self,text="CLEAR", width=12, pady=15, fg="White",font=("Bebas", "9" ,"bold" ), bg="#a45a52",command= lambda:self.clearall())
		clearbutt.grid(row=5, column=1, padx=3, pady=3)
		
		deletebutt = Button(self,text="DEL", width=12, pady=15, fg="White",font=("Bebas", "9" ,"bold" ), bg="#a45a52",command= lambda:self.delonecharac())
		deletebutt.grid(row=5, column=2, padx=3, pady=3)

		Pi_answer = "3.14"
		Pibutt = Button(self, text="π", width=12, pady=15, fg="Black", font=("Arial", "9", "bold"), bg="#b0b8ce", command=lambda: self.click(Pi_answer))
		Pibutt.grid(row=4, column=1, padx=3, pady=3)

		doublezerobutt = Button(self, text="00", width=12, pady=15, fg="Black", font=("Bebas", "9", "bold"), bg="#b0b8ce", command=lambda: self.click("00"))
		doublezerobutt.grid(row=4, column=2, padx=3, pady=3)
	

a = Calculator()
a.master.title("Tetrapython Brigade")
a.master.geometry("458x410")
a.configure(bg='#022954')
a.mainloop()

