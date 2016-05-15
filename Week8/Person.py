"""
Class: Person
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks, supplied by Faculty
This Class will store information about Person objects entered, including the following.

-First Name
-Last Name
-Age

Includes a String method for specific print formatting
"""
__Author__ = "Nicholas Stanton-Cook"


class Person:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """
        Define the formatting for printing to screen
        :return: String formatting
        """

        return "Name: {} {}, \nAge: {}".format(self.first_name, self.last_name, self.age)