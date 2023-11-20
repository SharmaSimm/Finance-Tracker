"""
Activity.py defines the 'Activity' subclass of 'Expenses', focusing on activity -related expenses. 
It includes location details and overrides the string representation to display the activity type,
location and amount. The class showcases Python inheritance by extending the 'Expenses' class for specific activity expenses.


"""
import Expenses

class Activity(Expense)
  def __init__(self, location = "", amount = 0.0):
    super().__init__("Activity", amount)
    self._location = location

  def __str__(self):
    return f"{self_category} at {self._location}: $ {self._amount}"
