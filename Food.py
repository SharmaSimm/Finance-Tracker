
import Expenses

class Food(Expenses):
  def __init__(self, name = "", amount = 0.0):
    super().__init__("Food", amount)
    self._name = name

  def __str__(self):
    return f"{self.category} ( {self.name} ) : $ {self.amount}"