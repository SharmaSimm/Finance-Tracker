"""
Bill.py defines the Bill class as a subclass of 'Expenses',specifically for handling bill payments.
tThe class constructors sets the expense category to "Bill" & accepts a company name and amount. 
It provides a customized string representation that includes the company name and bill amount. 
This class illustrates the application of inheritance in Python, extending Expenses class to cater to a specific type of financail activity. 

"""
import Expenses

class Bill(Expenses):
  
  def __init__(self, company = "", amount = 0.0):
    super().__init__("Bill", amount)
    self._company = company

  
  def __str__(self):
    return f"{self._company}: $ {self._amount}"
