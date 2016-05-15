"""
Program: Driving_simulator
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks

This program will allow the user to create a new Car with a customizable name, allocate them an amount of fuel and an
empty Odometer (set to 0) and allow them to simulate driving this car.

The function will include in the menu, the following options.

- Drive
    this will allow the user to drive the car a specified distance

- Refuel
    this will allow the user to fill up the car's fuel reserve.
"""
from Car import *

__Author__ = "Nicholas Stanton-Cook"


def main():
    """
     This function will control the menu and basic input error checking.
    """
    """
    print welcome message

    new_car_name = input
    [Error Check for blank string]

    current_car = instance of Car class with (name= new_car_name, fuel= 100)

    print current_car statistics
    print Menu
    menu_choice = input
    [Error check for capital or lower case input]

    while menu_choice does not = "Quit"
        if menu_choice = "Drive"

            run drive_the_car(current_car

        else if menu_choice = "Refuel"

            run refuel_the_car(current_car)

        else
            print invalid menu selection string

        print current_car statistics
        print Menu
        menu_choice = input
        [Error check for capital or lower case input]

    print goodbye message
    """

    print("\nLet's Drive!")

    new_car_name = input("Enter your car name: ")
    while new_car_name == "":
        print("Car name cannot be blank")
        new_car_name = input("Enter your car name: ")

    current_car = Car(100, new_car_name)

    main_menu = "\nMenu:\n(D)rive \n(R)efuel\n(Q)uit"

    print("\n{}".format(current_car))
    print(main_menu)
    chosen_menu_option = input('\nEnter your choice: ')
    chosen_menu_option = chosen_menu_option.upper()

    while chosen_menu_option != 'Q':
        if chosen_menu_option == 'D':

            current_car = drive_the_car(current_car)

        elif chosen_menu_option == 'R':

            current_car = refuel_the_car(current_car)

        else:
            print("Invalid choice")

        print("\n{}".format(current_car))
        print(main_menu)
        chosen_menu_option = input('\nEnter your choice: ')
        chosen_menu_option = chosen_menu_option.upper()

    print("Goodbye {}'s Driver".format(current_car.name))


def drive_the_car(car_to_drive):
    """
    This function is responsible for collecting the inputs and error checking them, then using those inputs to run
     the self.drive method of the Car class. It will also print the results with basic formatting.

    :param car_to_drive:
    :return: car_to_drive
    """
    """
    kilometers_to_drive = input
    [Error check for blank string]
    [Error check for correct (float) type]
    [Error check for input > 0]

    distance_driven = car_to_drive [drive method (kilometers_to_drive)]

    if current_car fuel = 0
        print formatted distance driven and out of fuel message
    else
        print formatted distance driven message

    return car_to_drive
    """
    print("How many Kilometers do you wish to drive?")

    error_marker = 0
    while error_marker == 0:

        try:
            kilometers_to_drive = float(input(":"))
            while kilometers_to_drive <= 0:
                print("Distance must be >= 0")
                kilometers_to_drive = float(input(":"))

            error_marker = 1
        except ValueError:
            print("Invalid Input\nPlease enter a valid number")
            error_marker = 0

    distance_driven = car_to_drive.drive(kilometers_to_drive)

    if car_to_drive.fuel == 0:
        print("The car drove {}km, and ran out of fuel.".format(str(distance_driven)))

    else:
        print("The car drove {}km.".format(str(distance_driven)))

    return car_to_drive


def refuel_the_car(car_to_refuel):
    """
    This function is responsible for collecting Inputs and error checking them, then running the self.add_fuel method
    of the Car class. It also has basic formatted printing of results.
    :param car_to_refuel:
    :return: car_to_refuel
    """
    """
    fuel_to_add = input
    [Error check for blank string]
    [Error check for correct (float) type]
    [Error check for input > 0]

    car_to_refuel [add_fuel method (fuel_to_add)]

    print formatted message for amount of fuel added

    return car_to_refuel
    """
    print("How many units of fuel do you want to add to the car?")

    error_marker = 0
    while error_marker == 0:

        try:
            fuel_to_add = float(input(":"))

            if fuel_to_add <= 0:
                while fuel_to_add <= 0:
                    print("Fuel amount must be >= 0")
                    fuel_to_add = float(input(":"))

            error_marker = 1

        except ValueError:
            print("Invalid Input\nPlease enter a valid number")
            error_marker = 0

    car_to_refuel.add_fuel(fuel_to_add)
    print("Added {} units of fuel.".format(str(fuel_to_add)))

    return car_to_refuel

main()
