"""
Food.py creates the Food class, a subclass of Expenses, dedicated to tracking food-related expenses.
It adds a specific food item name to the expense details and customizes the string representation
to include both the food category and the item name, along with the expense amount.
This class exemplifies Python inheritance, extending the Expenses class functionality to cater specifically to food expenses.


"""
import Expenses

class Food(Expenses):
  def __init__(self, name = "", amount = 0.0):
    super().__init__("Food", amount)
    self._name = name

  def __str__(self):
    return f"{self.category} ( {self.name} ) : $ {self.amount}"
