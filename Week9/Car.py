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


Inheritance Class: Taxi
Author: Nicholas Stanton-Cook
Program Set: Week nine Workshop Tasks, supplied by Faculty
This Class will Inherit information and methods from the Car class and add the following

new Parameters
-price_per_kilometer
-current_fare_distance

Changes to existing Methods
-Overrides the __str__ method to display the original Car __Str__ method plus the following
    -price per Km
    -current fare distance

-Changes the drive() method to include details about the current fare distance

New Methods
-get_fare()
    gets the total cost of the current fare
-start_fare()
    resets the values of current_fare_distance
"""
from random import random, randint
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


class Taxi(Car):
    PRICE_PER_KM = 1.20

    def __init__(self, fuel, name):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(fuel, name)
        self.price_per_km = Taxi.PRICE_PER_KM
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), self.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class UnreliableCar(Car):

    def __init__(self, fuel, name, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        float_number = random()
        whole_number = randint(0, 100)
        reliability_chance = float_number + whole_number
        if reliability_chance < self.reliability:
            distance_driven = super().drive(0)
        else:
            distance_driven = super().drive(distance)
        return distance_driven


class SilverServiceTaxi(Taxi):
    FLAGFALL_CHARGE = 4.50

    def __init__(self, fuel, name, fanciness):
        super().__init__(fuel, name)
        self.fanciness = fanciness
        self.flagfall = SilverServiceTaxi.FLAGFALL_CHARGE

    def get_fare(self):
        """ get the price for the taxi trip """
        return ((self.price_per_km * self.fanciness) * self.current_fare_distance) + self.flagfall


def Limousine(SilverServiceTaxi):

    def __init__(self, fuel, name, fanciness):
        super().__init__(fuel, name, fanciness)
        self.flagfall = (SilverServiceTaxi.FLAGFALL_CHARGE * 5)
        self.extra_services = randint(10, 100)

    def get_fare(self):
        """ get the price for the taxi trip """
        return ((self.price_per_km * self.fanciness) * self.current_fare_distance) + self.flagfall + self.extra_services


def ArmoredVehicle(Car):

    def __init__(self, fuel, name, callsign, armor, weapon):
       super().__init__(fuel, name)
       self.callsign = callsign
       self.armor = armor
       self.weapon = weapon

    def drive(self, distance):
        """
        drive the car a given distance if it has enough fuel
        or drive until fuel runs out
        return the distance actually driven
        """
        if (distance + self.armor/5) > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= (distance + self.armor/5)
        self.odometer += distance
        return distance

    def __str__(self):
        """
        Define the formatting for printing to screen
        :return: String formatting
        """

        return "CallSign:{} Armored Vehicle Model:{}, Fuel = {}, Odometer = {}, Armor = {}\nCurrent Payload = {}"\
            .format(self.callsign, self.name, self.fuel, self.odometer, self.armor, self.weapon)
