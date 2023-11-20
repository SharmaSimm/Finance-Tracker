
import Expenses

class Activity(Expense)
  def __init__(self, location = "", amount = 0.0):
    super().__init__("Activity", amount)
    self._location = location

  def __str__(self):
    return f"{self_category} at {self._location}: $ {self._amount}"