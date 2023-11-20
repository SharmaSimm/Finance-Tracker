"""
This class serves as a foundational structure for tracking various financial activites,
including bills,activites and food expenses. It allows for the addition of expenses by type,
with optional parameters for company, location and name. The class also include getters and setters for category and amount. 
Key functionality invloves categorizing and summing expenses, demonstrated through an intuitive method.


"""
class FinancialActivity:
  def __init__(self,category= "", amount = 0.0):
    self._category = category
    self._amount = amount

  def __str__(self):
    return f"{self._category}: $ {self._amount}"

  def add_expenses(self, expense_type, company = None, location = None, name = None, amount = 0.0):
    expenses = None
    if expense_type == "bill":
      expenses = Bill(company = company, amount = amount)
    elif expense_type == "activity":
      expenses = Activity(location = location , amount = amount)
    elif expense_type == "food":
      expenses = Food(name= name, amount=amount)

    if expenses:
      self._expenses.append(expenses)
      category = expenses._category  
      if category not in self._expenses_categories:
          self._expenses_categories[category] = 0
      self._expenses_categories[category] += expenses._amount  
      print(f"Added {expenses}")
    else:
      print("Invalid expense type")
  ##Getters
  def get_category(self):
    return self._category
  def get_amount(self):
    return self._amount
  ##Setters
  def set_category(self,category):
    self._category = category
  def set_amount(self,amount):
    self._amount = amount
