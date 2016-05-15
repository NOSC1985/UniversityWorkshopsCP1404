"""
Program: memberwise_addition
Author: Nicholas Stanton-Cook
Program Set: Week five Workshop Tasks
This function will take two lists of integers (assume error checking will be done externally)
The function will then add each logical position in the first list to its partner in the second list and
return the new list of values generated
"""
__Author__ = "Nicholas Stanton-Cook"

def memberwise_addition(number_list_one, number_list_two):
    memberwise_added_list = []

    if len(number_list_one) == len(number_list_two):
        for i in range(0, len(number_list_one), 1):
            memberwise_added_list.append(number_list_one[i]+number_list_two[i])

    elif len(number_list_one) > len(number_list_two):
        for i in range(0, len(number_list_two), 1):
            memberwise_added_list.append(number_list_one[i]+number_list_two[i])
        for i in range(len(number_list_two), len(number_list_one), 1):
            memberwise_added_list.append(number_list_one[i])
    elif len(number_list_one) < len(number_list_two):
        for i in range(0, len(number_list_one), 1):
            memberwise_added_list.append(number_list_one[i]+number_list_two[i])
        for i in range(len(number_list_one), len(number_list_two), 1):
            memberwise_added_list.append(number_list_two[i])

    return memberwise_added_list

