"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      self.cache[self.name] = self

    def add_stock(self, amount):
      self.qty += amount

    def sell(self, amount):
      if self.qty == 0:
        return print('Sorry, these cupcakes are sold out')

      if amount > self.qty:
        self.qty = 0
        return 

      self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
      ing_one, ing_two = ingredients

      ing_one_amount = ing_one[1]
      new_ing_one_amount = ing_one_amount*amount

      ing_two_amount = ing_two[1]
      new_ing_two_amount = ing_two_amount*amount

      scaled_recipe = [(ing_one[0], new_ing_one_amount), (ing_two[0], new_ing_two_amount)]

      return scaled_recipe

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
