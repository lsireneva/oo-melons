
from random import choice
from datetime import datetime

class Error(Exception):
    pass

class TooManyMelonsError(Error):
    def __init__(self):
     super().__init__("No more than 100 melons!")
        

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        try:
            if qty > 100:
                raise TooManyMelonsError()
            else:
                self.qty = qty
        except TooManyMelonsError:
            print("No more than 100 melons!")


    def get_total(self):
        """Calculate price, including tax."""
       
        total = (1 + self.tax) * self.qty * self.get_base_price()

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_base_price(self):
        splurge_fee = choice(range(5,10))
        now = datetime.now()

        if self.species == "Christmas Melons":
            base_price = splurge_fee*1.5
        else:
            base_price = splurge_fee
        
        #Rush Hour Prices
        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

        return base_price

"""Classes for melon orders."""

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)

    def get_total(self):
        return super().get_total()



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        if self.qty < 10:
            return  super().get_total() + 3
        else:
            return super().get_total()


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0)
        self.pass_inspection = False
    
    def mark_inspection(self, passed):
        self.pass_inspection = passed




