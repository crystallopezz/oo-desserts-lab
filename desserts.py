"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    #a dictionary that will store all cupcake instances by name
    cache = {}

    def __init__(self, name, flavor, price):
      """Set the name, flavor, and price of this cupcake. Also, set self.qty to 0"""
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      self.cache[self.name] = self

    def add_stock(self, amount):
      '''increase qty of cupcake by input amount'''

      self.qty += amount

    def sell(self, amount):
      '''Sell the given amount of cupcakes and update self.qty.'''

      # if cupcakes sold out, print an apology
      if self.qty == 0:
        return print('Sorry, these cupcakes are sold out')

      # if amount requested to be sold greater than the qty, only sell the available amt
      if amount > self.qty:
        self.qty = 0
        return 

      # if other conditions not met, subtract the requested amount from qty
      self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
      '''Take in  and scale list of ingredient tuples by the given integer of cupcakes.'''

      #unpack list of ingredients
      ing_one, ing_two = ingredients

      #get the amount of first ingredient
      ing_one_amount = ing_one[1]

      #increase first ingredient amount for number of cupcakes
      new_ing_one_amount = ing_one_amount*amount

      #repeat above two steps for second ingredient
      ing_two_amount = ing_two[1]
      new_ing_two_amount = ing_two_amount*amount

      #create new ingredient list
      scaled_recipe = [(ing_one[0], new_ing_one_amount), (ing_two[0], new_ing_two_amount)]


      # refactor would iterate through list of ingredients
      return scaled_recipe


    @classmethod
    def get(cls, name):
      '''Return a cupcake from cls.cache.'''

      dictionary = cls.cache
      apology = "Sorry, that cupcake doesn't exist"

      # if name doesn't exist, print the apologu
      if dictionary.get(name, False) == False:
        return print(apology)

      # if name does exist, return the dictionary entry
      return dictionary[name]



    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
