import unittest
import tkinter 
import _tkinter
from CalcLogic import Calculator

class Logic_Gui_Test(unittest.TestCase):

	def Final_Test(self):
		while self.a.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
			pass

	def setUp(self):
		self.a=tkinter.Tk()
		self.Final_Test()

	def SetUp_1(self):
		if self.a:
			self.Final_Test()

class TetrapythBrigadeTest(Logic_Gui_Test):
	
	def test_Error1(self):
		c = Calculator(self.a)
		self.Final_Test()
		problem = '1/0'
		c.click(problem)
		self.assertEqual(c.problem.get(), problem)
		wrong = "Error"
		c.click("1/0")
		c.solve()
		self.assertEqual(c.problem.get(), wrong)

	def test_Error2(self):
		c = Calculator(self.a)
		self.Final_Test()
		problem = '1+*-'
		c.click(problem)
		self.assertEqual(c.problem.get(), problem)
		wrong = "Error"
		c.click("1/0")
		c.solve()
		self.assertEqual(c.problem.get(), wrong)

	def test_Error3(self):
		c = Calculator(self.a)
		self.Final_Test()
		problem = '*6'
		c.click(problem)
		self.assertEqual(c.problem.get(), problem)
		wrong = "Error"
		c.click("*6")
		c.solve()
		self.assertEqual(c.problem.get(), wrong)

	def test_Error4(self):
		c = Calculator(self.a)
		self.Final_Test()
		problem = '/6'
		c.click(problem)
		self.assertEqual(c.problem.get(), problem)
		wrong = "Error"
		c.click("/6")
		c.solve()
		self.assertEqual(c.problem.get(), wrong)

	def test_Positive(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "6"
		c.click("+6")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_Negative(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "-6"
		c.click("-6")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_Addition(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "6"
		c.click("1+2+3")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_Subtraction(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "0"
		c.click("1-1")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_Division(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "1.0"
		c.click("1/1")
		c.solve()
		self.assertEqual(c.problem.get(), result)
	
	def test_Multiplication(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "1"
		c.click("1*1")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_Mix(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "5.0"
		c.click("6+5-4*3/2")
		c.solve()
		self.assertEqual(c.problem.get(), result)

	def test_delete(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = "12345"
		c.click("123456")
		c.delonecharac()
		self.assertEqual(c.problem.get(), result)

	def test_clearall(self):
		c = Calculator(self.a)
		self.Final_Test()
		result = ""
		c.click("123456")
		c.clearall()
		self.assertEqual(c.problem.get(), result)



if __name__ == '__main__':
    import unittest
    unittest.main()
