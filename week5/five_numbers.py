"""
Program: five_numbers
Author: Nicholas Stanton-Cook
Program Set: Week five Workshop Tasks
This program will ask the user for an input of five numbers and then
show the user data about that Number set including the following.
The first number entered, The last Number Entered, the Lowest Number, The Highest Number, the average of all the numbers
"""
__Author__= "Nicholas Stanton-Cook"

def main():
    """Function: Main
    This function runs the function get_five_numbers_user_input() to get a set of five numbers from the user and
    calculates the desired data regarding the list.
    It then prints the desired values to the screen
    :return:
    """
    """
    get five numbers from user

    first_number = first number entered
    last_number = last number entered
    highest_number = highest value number entered
    lowest_number = lowest number entered
    average_numbers = average of the list.

    print data to screen
    """
    number_set = get_five_numbers_from_user_input()

    first_number_in_set = number_set[0]
    last_number_in_set = number_set[-1]
    highest_number_in_set = max(number_set)
    lowest_number_in_set = min(number_set)
    average_of_number_set = (sum(number_set)/(len(number_set)))

    print("The first number is {}\nThe last number is {}\nThe smallest number is {}\n"
          "The largest number is {}\nThe average of the numbers is {}".format(first_number_in_set, last_number_in_set,
                                                                              lowest_number_in_set,
                                                                              highest_number_in_set,
                                                                              average_of_number_set))


def get_five_numbers_from_user_input():
    """Function: get_five_numbers_from_user_input
    This function will error check and gather user inputs for a list of five numbers.
    Note: Can be extended easily to include larger lists.
    :return: number_list
    """
    """
    for i (0-max)
        next_number = input
        Error check for blank or invalid type, must be float or int

        add next_number to numbers_list

    return numbers_list
    """
    maximum_list_length = 5
    numbers_list = []
    error_marker = 0
    for i in range(0, maximum_list_length, 1):
        while error_marker == 0:
            try:
                next_number = float(input("Number: "))

                if next_number == "":
                    while next_number == "":
                        print("input cannot be blank!")
                        next_number = input("Number: ")

                error_marker = 1
            except ValueError:
                print("Please enter a valid number")
                error_marker = 0

        numbers_list.append(next_number)
        error_marker = 0
    return numbers_list


main()