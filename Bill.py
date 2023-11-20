import Expenses

class Bill(Expenses):
  
  def __init__(self, company = "", amount = 0.0):
    super().__init__("Bill", amount)
    self._company = company

  
  def __str__(self):
    return f"{self._company}: $ {self._amount}"
