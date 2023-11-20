"""
This class manages individual expense records. The class encapsulates expense details such as category and amount, 
offering both getters and setters for these properties. Its key functionality lies in enabling the creation 
and manipulation of expense data, effectively represented through a clear string output format. 
This class forms an integral part of a larger financial management system, using basic principles of OOP IN Python. 


"""
class Expenses():


  ##constructor with default parameter
    def __init__(self, cateregory = "", amount = 0.0):
      self._category = cateregory
      self._amount = amount

    def __str__(self):
      return f"{self._category}: $ {self._amount}"

  ####Getters ####

    def get_category(self):
      return self._category
    def get_amount(self):
      return self._amount

  ####Setters #####
    def set_category(self,category):
      self._category = category

    def set_amount(self,amount):
      self._amount = amount
