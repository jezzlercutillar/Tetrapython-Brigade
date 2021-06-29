#Try lang
import unittest
from Logic import Calculator

class Test(unittest.TestCase):
  def test_00_addition(self):
    solve = "1+1"
    self.assertEqual(Calculator(Solve), 2)

  def test_00_addition(self):
    solve = "1+1+1+1"
    self.assertEqual(Calculator(Solve), 4)
    
  def test_00_subtraction(self):
    solve = "5-3"
    self.assertEqual(Calculator(Solve), 2) 

  def test_00_subtraction(self):
    solve = "50-6-5-4-2-1"
    self.assertEqual(Calculator(Solve), 32)

  def test_00_multiplication(self):
    solve = "5*10"
    self.assertEqual(Calculator(Solve), 50)
 
  def test_00_multiplication(self):
    solve = "1*5*53*6"
    self.assertEqual(Calculator(Solve), 1590)
    
  def test_00_division(self):
    solve = "138/2"
    self.assertEqual(Calculator(Solve), 69)
    
  def test_00_division(self):
    solve = "138/2/3"
    self.assertEqual(Calculator(Solve), 23)
    
   def test_00_mix(self):
    solve = "1+2*3/4"
    self.assertEqual(Calculator(Solve), 2.5)
    
   def test_00_mix_1(self):
    solve = "1/2*3-4"
    self.assertEqual(Calculator(Solve), -2.5)  
  
if __name__ == "__main__":
  unittest.main()
