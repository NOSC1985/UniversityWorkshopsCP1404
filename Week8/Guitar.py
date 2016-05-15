"""
Class: Guitar
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks
This Class will store information about guitars entered including the following.

-Make
-Model
-Year Made
-Price

Includes the following Methods

get_age(self)
This method will return and integer for the age of the guitar in years

is_vintage(self)
This method will return a boolean True of False depending on if the guitar is currently older than 50 years

This class also includes a String method for formatting printing.
"""
__Author__ = "Nicholas Stanton-Cook"

CURRENT_YEAR = 2016


class Guitar:
    """
    Define the Base parameters
    """
    def __init__(self, make="", model="", year=0, price=0):

        self.make = make
        self.model = model
        self.year_made = year
        self.price = price

    def get_age(self):
        """
        Calculate the age of the guitar in years by subtracting the year made from the CURRENT_YEAR
        """
        years_old = CURRENT_YEAR - self.year_made

        return years_old

    def is_vintage(self):
        """
        if age < 50
            return boolean False
        else
        return boolean True
        """

        if self.get_age() < 50:
            return False
        else:
            return True

    def __str__(self):
        """
        if Guitar is Vintage
            vintage_string = "(vintage)"
        else
            vintage_string = " "

        format string to specified format

        :return: formatted String
        """
        if self.is_vintage():
            vintage_string = "(vintage)"

        else:
            vintage_string = ""

        return "{:>20} ({}), worth ${:1,.2f} {}".format(self.make + ", " + self.model, self.year_made, self.price,
                                                         vintage_string)
