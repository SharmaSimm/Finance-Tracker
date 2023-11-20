

"""

Personal Finance Tracker Program.



This program allows a user to manage their finances by tracking their budget, expenses, and savings goals. 
Users can interact with a simple text to manage various financial categories, view summaries and perform operations to calculate their financial status.
"""

##########################################
# IMPORTS:

import Budget
import Expenses
from FinanceTracker import FinanceTracker
import FinancialActivity

######################################
##########################################
# MAIN PROGRAM:
##Execute the Personal Finance Tracker Program. It provides a user interface for interacting with the financial tracker, allowing user to add expenses, view expenses, edit expenses, view budget, and  set savings goals.
##########################################
def main():
  
  tracker = FinanceTracker()
##Displaying welcome message and instruction to the user
  print("Welcome to Personal Finance Tracker ! \n")
  print("Instructions: ")
  print("1. Set your monthly budget")
  print("2. Record an expenses")
  print("3. Set a savings goal")
  print("4. View financial summary")
  print("5. Exit the tracker \n")

  ###Main loop to keep the program running until the user chooses to quites
  while True:
    #User input to choose an option
    choice = input("Enter your choice (1-5) :")
##Setting budget, it allows the user to input a new budget amount
    if choice == "1":
      try:
        amount = float(input("Enter your monthly budget: "))
        if amount < 0: 
          raise ValueError("Budget cannot be negative")
        tracker.set_budget(amount)
      except ValueError: 
        print("Invalid input. Please enter a number")
      # tracker.set_budget(amount)
  ##Recording expenses, it allows user to input expenses category and amount
    elif choice == "2":
      expense_type = input("Enter the type  of the expenses (bill, activity, food): ")
      amount = float(input(f"Enter the amount of the {expense_type} : "))
      # try:
      #   amount = float(input("Enter the amount of the expense: "))
      #   if amount < 0: 
      #     raise ValueError("Expense cannot be negative")

      if expense_type == "bill":
        company = input("Enter the company name: ")
        tracker.add_expense(expense_type, company=company, amount=amount)
      else:
        tracker.add_expense(expense_type, amount=amount)
    
      #   tracker.add_expense(category.strip(), amount)
      # except ValueError:
      #   print(f"Invalid input. Please enter a number for {category}")
        
  ##Setting savings goal and allowing the user to input a savings goal amount
    elif choice == "3":
      try: 
        amount = float(input("Enter your savings goal $: "))
        if amount < 0:
          raise ValueError("Saving goal cannot be negative")
        tracker.set_savings_goal(amount)
      except ValueError:
        print("Invalid input.")
  ##View Summary: Display a summary of the current fiancial status of the user
    elif choice == "4":
      tracker.summary()
  ##Exit the tracker. Break the loop and exit the program
    elif choice == "5":
      print("Thank you for using Personal Finance Tracker. Have a great day")
      break
  ##Handles invalid input
    else:
      print("Opps... Please enter the number between 1-5")
  
if __name__ == "__main__":
  main()
