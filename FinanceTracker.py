

class FinanceTracker:
  ##constructor
  def __init__(self, budget=0, expenses=None, expenses_categories=None, savings_goal=0):
    if expenses is None:
      expenses = []
    if expenses_categories is None:
      expenses_categories = {}
    self._budget = budget
    self._expenses = expenses
    self._expenses_categories = expenses_categories
    self._savings_goal = savings_goal

########Getters
  def get_budget(self):
    return self._budget

  def get_expenses(self):
    return self._expenses

  def get_expenses_categories(self):
    return self._expenses_categories

  def get_savings_goal(self):
    return self._savings_goal

    # Mutators/Setters

  def set_budget(self, amount):
    self._budget = amount
    print(f"Budget set to ${amount} ")

  def set_expenses(self, expenses):
    self._expenses = expenses

  def set_expenses_categories(self, expenses_categories):
    self._expenses_categories = expenses_categories

  def set_savings_goal(self,amount):
    self._savings_goal = amount
    print(f"Savings goal set to ${amount}")
  
  def __str__(self):
    return (f"Budget: ${self._budget}\n"
            f"Total Expenses: ${sum(amount for _, amount in self._expenses)}\n"
            f"Savings Goal: ${self._savings_goal}\n"
            f"Expense Categories: {self._expenses_categories}\n")
  
#####Add method
  def add_expense(self, category, amount, company = None):
    if company:
      self._expenses.append((category, amount, company))
    else:
      self._expenses.append((category, amount))
    if category not in self._expenses_categories:
      self._expenses_categories[category] = 0
    self._expenses_categories[category] += amount
    print(f"Added ${amount} expense under {category}")
    if company:
      print(f"Added ${amount} {category} expense for {company}.")
    else:
      print(f"Added ${amount} expense under {category}")

  def summary(self):
    print("\n ---- Financial Summary ---")
    print(f"Total Budget : ${self._budget}")
    total_expense = sum(amount for _, amount, *_ in self._expenses) 
    print(f"Total Expenses: ${total_expense}")
    for category, amount in self._expenses_categories.items():  
        print(f"{category}: ${amount}")
    print(f"Savings Goal: ${self._savings_goal}")  
    print(f"Remaining Balance : ${self._budget} - {total_expense}")
    if self._budget > total_expense:
      print("You are under budget")
    else:
      print("You are over budget")
    print("-----------------------------")

