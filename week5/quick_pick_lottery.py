"""
Program: quick_pick_lottery
Author: Nicholas Stanton-Cook
Program Set: Week five Workshop Tasks
This program will ask the user for an input of how many Quick-Pick lottery number sets they want,.
then generate that many randomized sets of six numbers, each number in each set will be between 1 and 45.
Each set must be displayed in ascending order
"""
__Author__= "Nicholas Stanton-Cook"
from random import *

"""
number_of_quick_picks = user input
Error check for blank string
Error check for numbers <= 0
Error check for incorrect data type, must be int

for (1 to (number_of_quick_picks))
    current_list = blank list
    for (1 to 6)
        random_number = (random integer between 1 and 45)

        if (random_number) already in (current_list)
            while (random_number) already in (current_list)
                random_number = (random integer between 1 and 45)

        add (random_number) to (current_list)

    sort (current_list) in ascending order
    print (current_list) 
"""
error_marker = 1
while error_marker == 1:
    try:
        requested_quick_picks = int(input("How many Quick Picks?: "))
        if requested_quick_picks == "":
            while requested_quick_picks == "":
                requested_quick_picks = int(input("Must enter a valid number\nHow many Quick Picks?: "))

        elif requested_quick_picks <= 0:
            while requested_quick_picks <= 0:
                requested_quick_picks = int(input("Must enter a number greater than zero\nHow many Quick Picks?: "))

        error_marker = 0
    except ValueError:
        print("Please enter a valid number")
        error_marker = 1

maximum_range = requested_quick_picks

for n in range(0, maximum_range, 1):
    current_list = []
    for i in range(0, 6, 1):

        randomized_number = randint(1, 45)

        if randomized_number in current_list:
            while randomized_number in current_list:
                randomized_number = randint(1, 45)

        current_list.append(randomized_number)

    current_list.sort()
    print("{} {} {} {} {} {}".format(current_list[0], current_list[1], current_list[2], current_list[3], current_list[4], current_list[5]))

