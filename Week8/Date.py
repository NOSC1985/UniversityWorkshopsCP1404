"""
Class: Date
Author: Nicholas Stanton-Cook
Program Set: Week eight Workshop Tasks
This Class will store information about calendar Dates and will include the following information.

-day_of_month
-month_in_year
-year

Includes the following Methods

add_days(self, amount)
This method will increase the calendar days by the specified amount, increasing the Month and year as necessary.

also includes a String method for specific print formatting
"""

__Author__ = "Nicholas Stanton-Cook"

MONTHS_LIST = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]


def check_leap_year(year_to_check):
            """Function: check_leap_year()
            This function uses the official determination for leap years to check if any specific year will be a leap year.
            By first checking if the year is evenly divisible by 4, then checking if the year is NOT evenly divisible by 100,
            unless the year is evenly divisible by 400.
            :param year_to_check:
            :return: checker
            """
            """
            if year/4 remainder = 0
                if year/100 remainder = 0
                    checker = no

                    if year/400 remainder = 0
                        checker = yes
                else
                    checker = yes
            else
                checker = no

            """
            if (year_to_check % 4) == 0:
                if (year_to_check % 100) == 0:
                    checker = 0
                    if (year_to_check % 400) == 0:
                        checker = 1
                else:
                    checker = 1
            else:
                checker = 0

            return checker


class Date:
    def __init__(self, day, month, year):
        """
        initialize the parameters, assuming error checking for original dates is done in upper level program.

        Example of correct error checking in upper levels:
        [sample taken from "dictionary_of_names_and_ages.py", from 'Week 7 workshop tasks']
        ################################################################################################################
        new_name = input("Enter Name: ")
        while new_name == "":
            print("Name Cannot Be Blank!")
            new_name = input("Enter Name: ")
            error_marker = 0
        while error_marker == 0:
            try:
                year_born = int(input("Enter Year of Birth: "))
                month_born = int(input("Enter the number of the Month of Birth (between 1 and 12): "))
                if (month_born > 12) or (month_born < 1):
                    print("Invalid Date!, Must enter a month Between 1 and 12\nPlease Try Again!")
                    while (month_born > 12) or (month_born < 1):
                        month_born = int(input("Enter the number of the Month of Birth (between 1 and 12): "))
                day_born = int(input("which Day of {} was {} Born in {}: ".format(MONTHS_LIST[month_born-1], new_name,
                                                                              year_born)))
                error_marker = 1
            except ValueError:
                print("Please enter a Valid Number!")
                error_marker = 0

            if year_born > CURRENT_YEAR:
                print("Cannot be born in the Future!!")
                error_marker = 0
            elif (year_born == CURRENT_YEAR) and (month_born > CURRENT_MONTH):
                print("Cannot be born in the Future!!")
                error_marker = 0
            elif (year_born == CURRENT_YEAR) and (month_born == CURRENT_MONTH) and (day_born > CURRENT_DAY):
                print("Cannot be born in the Future!!")
                error_marker = 0
            elif (month_born in [1, 3, 5, 7, 8, 10, 12]) and (day_born > 31):
                print("Invalid Day!, {} only has 31 days!\n Please Try Again!".format(MONTHS_LIST[month_born-1]))
                error_marker = 0
            elif (month_born in [4, 6, 9, 11]) and (day_born > 30):
                print("Invalid Day!, {} only has 30 days!\n Please Try Again!".format(MONTHS_LIST[month_born-1]))
                error_marker = 0
            elif (month_born == 2) and (check_leap_year(year_born) == 1) and (day_born > 29):
                print("Invalid Day!, {} only has 29 days in the year {} as it is a leap year!\n Please Try Again!"
                      .format(MONTHS_LIST[month_born-1], year_born))
                error_marker = 0
            elif (month_born == 2) and (check_leap_year(year_born) == 0) and (day_born > 28):
                print("Invalid Day!, {} only has 28 days in the year {} as it is not a leap year!\n Please Try Again!"
                      .format(MONTHS_LIST[month_born-1], year_born))
                error_marker = 0
            elif day_born < 1:
                print("Invalid Day!, Please Enter a positive number!")
                error_marker = 0

        names_and_dob_dict[new_name] = [day_born, month_born, year_born]
        return names_and_dob_dict
        ################################################################################################################
        :param day:
        :param month:
        :param year:
        :return:
        """
        """

        """

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
        This method formats the Date class for printing.
        :return: formatted_string
        """
        """
        pick strings from appropriate date formats
        """
        month = MONTHS_LIST[(self.month - 1)]

        if self.day in [1, 21, 31]:
            string = "{}st {} {}".format(self.day, month, self.year)

        elif self.day in [2, 22]:
            string = "{}nd {} {}".format(self.day, month, self.year)

        elif self.day in [3, 23]:
            string = "{}rd {} {}".format(self.day, month, self.year)

        elif self.day in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 30]:
            string = "{}th {} {}".format(self.day, month, self.year)

        return string

    def add_days(self, days_to_add):
        """
        This method will increase the calendar days by the specified amount, increasing the Month and year as necessary.
        :param days_to_add:
        """
        """
        loop for (days_to_add)

            if current_month has 31 days
                if current_day < 31
                    add +1 to current_day

                if current_day = 31
                    if current_month < 12
                        add +1 to current_month

                    else if current_month = 12
                        add +1 to current year
                        current_month = 1

                    current_day = 1

            else if current_month has 30 days
                if current_day < 30
                    add +1 to current_day

                if current_day = 30
                    if current_month < 12
                        add +1 to current_month

                    else if current_month = 12
                        add +1 to current year
                        current_month = 1

                    current_day = 1

            else if current_month = 2 and check_leap_year(current_year) = 1
                if current_day < 29:
                    add +1 to current_day

                elif self.day == 29:
                    if current_month < 12
                        add +1 to current_month

                    else if current_month = 12
                        add +1 to current year
                        current_month = 1

                    current_day = 1

            else if current_month = 2 and check_leap_year(current_year) = 0
                if current_day < 28:
                    add +1 to current_day

                elif self.day == 28:
                    if current_month < 12
                        add +1 to current_month

                    else if current_month = 12
                        add +1 to current year
                        current_month = 1

                    current_day = 1
        """
        for i in range(0, days_to_add, 1):

            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.day < 31:
                    self.day += 1

                elif self.day == 31:
                    if self.month < 12:
                        self.month += 1

                    elif self.month == 12:
                        self.year += 1
                        self.month = 1
                    self.day = 1

            elif self.month in [4, 6, 9, 11]:
                if self.day < 30:
                    self.day += 1

                elif self.day == 30:
                    if self.month < 12:
                        self.month += 1

                    elif self.month == 12:
                        self.year += 1
                        self.month = 1
                    self.day = 1

            elif (self.month == 2) and (check_leap_year(self.year) == 1):
                if self.day < 29:
                    self.day += 1

                elif self.day == 29:
                    if self.month < 12:
                        self.month += 1

                    elif self.month == 12:
                        self.year += 1
                        self.month = 1
                    self.day = 1

            elif (self.month == 2) and (check_leap_year(self.year) == 0):
                if self.day < 28:
                    self.day += 1

                elif self.day == 28:
                    if self.month < 12:
                        self.month += 1

                    elif self.month == 12:
                        self.year += 1
                        self.month = 1
                    self.day = 1





