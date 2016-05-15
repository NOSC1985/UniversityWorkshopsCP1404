"""
Program: playing_the_guitars
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks
This program will allow a user to input their Guitar collection and store that data in a list.
When the user has finished entering their collection, the program will print their listed guitars in a readable format
"""
from Guitar import *

__Author__ = "Nicholas Stanton-Cook"


def main():
    """
    This function will control the Menu functionality and error checking of Inputs
    """
    """
    Display Greeting Message

    While menu choice not equal to "Quit"

        new_guitar_make = input
        [Error Check for blank string]

        new_guitar_model = input
        [Error Check for blank string]

        new_guitar_year_made = input
        [Error Check for blank string]
        [Error Check for (new_guitar_year_made <= CURRENT_YEAR)]
        [Error Check for correct (integer) type]

        new_guitar_price = input
        [Error Check for blank string]
        [Error Check for (new_guitar_price > 0)]
        [Error Check for correct (float) type]

        new_guitar_list = new_guitar_make, new_guitar_model, new_guitar_year_made, new_guitar_price

        add new_guitar_list to guitars_list


    print_all_guitars(guitars_list)

    """

    print("Welcome to 'Playing My Guitars'\nA program by {}\n".format(__Author__))
    guitar_list = []
    run = "Y"
    while run != "N":

        new_guitar_make = input("Guitar Make: ")
        if new_guitar_make == "":
            while new_guitar_make == "":
                print("Invalid Input, Make cannot be Blank\n")
                new_guitar_make = input("Guitar Make: ")

        new_guitar_model = input("Guitar Model: ")
        if new_guitar_model == "":
            while new_guitar_model == "":
                print("Invalid Input, Model cannot be Blank\n")
                new_guitar_model = input("Guitar Model: ")

        error_marker = 0
        while error_marker == 0:
            try:
                new_guitar_year_made = int(input("Guitar Production Year: "))
                if new_guitar_year_made > CURRENT_YEAR:
                    while new_guitar_year_made > CURRENT_YEAR:
                        print("Sorry, No Future Guitars!!!")
                        new_guitar_year_made = int(input("Guitar Production Year: "))

                error_marker = 1

            except ValueError:
                print("Please enter only a Valid Year")
                error_marker = 0

        error_marker2 = 0
        while error_marker2 == 0:
            try:
                new_guitar_price = float(input("Guitar current Price: "))
                if new_guitar_price < 0:
                    while new_guitar_price < 0:
                        print("No Negative Prices Please!!!")
                        new_guitar_price = float(input("Guitar current Price: "))

                error_marker2 = 1

            except ValueError:
                print("Please enter only a Valid price")
                error_marker2 = 0

        new_guitar = Guitar(new_guitar_make, new_guitar_model, new_guitar_year_made, new_guitar_price)

        guitar_list.append(new_guitar)

        print("Would you like to enter another Guitar? (Y)es (N)o")
        entry = input(": ")
        entry = entry.upper()
        if entry == "Y":
            run = "Y"
        elif entry == "N":
            run = "N"
        else:
            invalid_input_marker = 0
            while invalid_input_marker == 0:
                print("Invalid selection!")
                print("Would you like to enter another Guitar? (Y)es (N)o")
                entry = input(": ")
                entry = entry.upper()

                if entry == "Y":
                    run = "Y"
                    invalid_input_marker = 1
                elif entry == "N":
                    run = "N"
                    invalid_input_marker = 1

    print_all_guitars(guitar_list)


def print_all_guitars(finished_guitar_list):
    """
    This function will correctly format and print to screen the completed list of Guitars
    :param finished_guitar_list:
    """
    """
    print title message to screen

    for guitar in finished_guitar_list
        print with required format

    """

    print("\nThese are my Guitars\n")
    counter = 1
    for guitar in finished_guitar_list:
        print("Guitar {}: {}".format(counter, guitar))
        counter += 1


main()
