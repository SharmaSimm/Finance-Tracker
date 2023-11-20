"""
Budget file extends the "FinancialActivity" class to include budgeting capabilities. 
It manages budget categories with spending limits, offering methods to set &retrieve these limits. 
The class provides a concise string representation of each budget category, its spending, and its maximum limits, 
demonstrating the use of inheritance in Python.



"""
from FinancialActivity import FinancialActivity

class Budget(FinancialActivity):

  ##default and full constructor
  def __init__(self, category = "", amount = 0.0 , max_limit = 0.0):
    super().__init__(category, amount)
    self._max_limit = max_limit

  def __str__(self):
    return f"{self._category}: $ {self._amount}, Max Limit : ${self._max_limit}"

####Getter & Setter
  def get_max_limit(self):
    return self._max_limit
    
  def set_max_limit(self, max_limit):
    self._max_limit = max_limit
    
