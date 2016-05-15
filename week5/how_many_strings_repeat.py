"""
Program: how_many_strings_repeat
Author: Nicholas Stanton-Cook
Program Set: Week five Workshop Tasks
This program will ask the user for an indefinite amout of strings until a blank string is entered and then
show the user any strings which were entered more than once.
"""
__Author__ = "Nicholas Stanton-Cook"

"""
while (new_string) not blank
    new_string = user input
    list-of_strings_entered = list_of_strings_entered + new_string

while length of list_of_strings_entered > 0
    string_to_check = list_of_strings_entered(first logical position)
    delete (list_of_strings_entered(first logical position))

    if string_to_check is still in list_of_strings_entered
        string_to_print = string_to_print + string_to_check
        remove all other instances of (string_to_check) from (list_of_strings_entered)

if string_to_print is blank
    string_to_print = "no repeated strings entered"

print string_to_print
"""
list_of_strings_entered = []
new_string = input("Please enter a string: ")
string_to_print = ""

while new_string != "":
    list_of_strings_entered.append(new_string)
    new_string = input("Please enter a string: ")

while len(list_of_strings_entered) > 0:
    current_string_to_check = list_of_strings_entered[0]
    del list_of_strings_entered[0]
    if current_string_to_check in list_of_strings_entered:
        string_to_print += (" " + current_string_to_check)
        while current_string_to_check in list_of_strings_entered:
            list_of_strings_entered.remove(current_string_to_check)

if string_to_print == "":
    string_to_print = "No repeated strings entered"
print("Strings repeated: {}".format(string_to_print))
