

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