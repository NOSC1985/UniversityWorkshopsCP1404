"""
Class: Car
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks, supplied by Faculty
This Class will store information about Car objects entered, including the following.

-Fuel
-Name
-Odometer

Includes the following Methods

add_fuel(self, amount)
This method will increase self.fuel by the specified parameter, (amount).

drive(self, distance)
This method will increase the cars odometer while subtracting the corresponding amount of fuel. The distance will
stop if the distance traveled exceeds the amount of fuel in the variable self.fuel

also includes a String method for specific print formatting
"""
__Author__ = "Original Author: CP1404 Faculty\nModified by: Nicholas Stanton-Cook"


class Car:
    def __init__(self, fuel=0, name=""):
        """ initialise a Car instance
        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):
        """
        add amount to the car's fuel
        """
        self.fuel += amount

    def drive(self, distance):
        """
        drive the car a given distance if it has enough fuel
        or drive until fuel runs out
        return the distance actually driven
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """
        Define the formatting for printing to screen
        :return: String formatting
        """

        return "{}, Fuel={}, Odometer={}".format(self.name, self.fuel, self.odometer)
