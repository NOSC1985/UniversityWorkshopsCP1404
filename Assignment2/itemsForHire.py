
"""Author: Nicholas Stanton-Cook
Dates: 31/3/2016 -> 4/4/2016
Description: This program allows a user to check and manage a list of items for sale, stored and retrieved from a
C.S.V formatted text file. The user is presented with a menu allowing them choices to diplay all items,
hire out an item, return an item, add a new item or quit. This will use an error checked menu structure to ensure
valid inputs.
git hub repository: https://github.com/NOSC1985/assignment1cp1404
"""
__Author__ = "Nicholas Stanton-Cook"
FILE_NAME = "items.csv"


def main(file_name):
    """
    :param file_name:
    :return:
    """
    """Function Main. generates the Menu and loads and saves the file. Responsible for the basic user selections.

    print welcome message

    import the file
    format the file date with (format_csv-file_data_for_use())
    close file

    print the number of items loaded from file.
    print the file name

    generate the main menu structure for printing
    print main menu to screen

    (chosen_menu_option) = user input
    Error check for upper and lower case inputs

    while (chosen_menu_option) does not = 'Q'
        if the chosen_menu_option = 'L'
            (print_items_list_all(print all))

        else if (chosen_menu_option) = 'H'
            (check_status_list) = (check_item_status(items_list, check for 'in' string))
            if (check_status_list) = 0
                print to screen ("No items available for hire")
            else if (check_status_list) = 1
                (print_items_list_all(print available only))
                (items_lists) = hire_item(items_lists)

        else if (chosen_menu_option) = 'R'
            (check_status_list) = (check_item_status(items_list, check for 'out' string))
            if (check_status_list) = 0
                print to screen ("No items on hire")
            else if (check_status_list) = 1
                (print_items_list_all(print unavailable only))
                (items_lists) = return_item(items_lists)

        else if (chosen_menu_option) = 'A'
            (items_lists) = (add_item(items_lists))

        else
            Error checking for invalid inputs
            print to screen ("invalid choice")

        print main menu to screen

        (chosen_menu_option) = user input
        Error check for upper and lower case inputs

    (save_file_data) = format_csv_file_data_to_save(items_lists)
    open file to write
    write (save_file_data) to file
    close file

    print to screen (filename and total items saved to file)

    finish main program!
    """
    print('Items for Hire - by:{}\n'.format(__Author__))

    import_file = open("{}".format(file_name), mode='r')
    items_lists = format_csv_file_data_for_use(import_file)
    import_file.close()

    items_loaded = len(items_lists)
    print("{} items loaded from {}".format(items_loaded, file_name))

    main_menu = "Menu:\n(L)ist all items \n(H)ire an Item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

    print(main_menu)

    chosen_menu_option = input('Input your selection: ')
    chosen_menu_option = chosen_menu_option.upper()

    while chosen_menu_option != 'Q':
        if chosen_menu_option == 'L':
            print("All items on file (* indicates item is currently out):")
            print_items_list_all(items_lists, 1)
        elif chosen_menu_option == 'H':
            print('Hire Item')
            check_status_list = check_item_status(items_lists,"in")

            if check_status_list == 0:

                print("No items available for hire")
            else:
                print_items_list_all(items_lists, 3)
                items_lists = hire_item(items_lists)

        elif chosen_menu_option == 'R':
            print('Return Item')
            check_status_list = check_item_status(items_lists,"out")

            if check_status_list == 0:

                print("No items are currently on hire")
            else:
                print_items_list_all(items_lists, 2)
                items_lists = return_item(items_lists)
        elif chosen_menu_option == 'A':
            print('Add Item')
            items_lists = add_new_item(items_lists)
        else:
            print("Invalid choice")

        print(main_menu)
        chosen_menu_option = input('Input your selection: ')
        chosen_menu_option = chosen_menu_option.upper()

    save_file_data = format_csv_file_data_to_save(items_lists)
    import_file = open("{}".format(FILE_NAME), mode='w')
    import_file.write(save_file_data)
    import_file.close()
    final_item_count = len(items_lists)
    print("{} items saved to {}\nHave a nice day :)".format(final_item_count, file_name))


def format_csv_file_data_for_use(imported_file):
    """
    :param imported_file:
    :return:
    """
    """Function to separate and format the CSV file data
    (whole_file_string) = file data as single string
    remove any blank space from start or end of (whole_file_string)
    (list_of_strings) = whole_file_string (with each line separated at \n character)

    for each (string) in (list_of_strings)
        update (list_of_strings) = (list_of_strings) - remove \n character

    for each (string) in (list_of_strings)
        (list_of_strings) = (list_of_strings(position(n))) - split each item in the (list_of_strings) into an internal
         list on the "," character

    return (list_of_strings) to main function
    """
    whole_file_string = imported_file.read()
    list_of_strings = whole_file_string.strip()
    list_of_strings = list_of_strings.split('\n')

    counter_strip = 0
    for n in list_of_strings:
        list_of_strings[counter_strip] = list_of_strings[counter_strip].strip()
        counter_strip += 1

    counter_split = 0
    for i in list_of_strings:
        list_of_strings[counter_split] = list_of_strings[counter_split].split(',')
        counter_split += 1
    return list_of_strings


def format_csv_file_data_to_save(finalized_list):
    """
    :param finalized_list:
    :return: string_to_save_to_file
    """
    """Function to concatenate and format the CSV file data for saving to file.
    get (finalised_list) from Main Function


    for each (list) in (finalized_list)
        (finalized_list(position(list)) = "(list(position(0)+(list(position(1)+(list(position(2))+(list(position(3)+\n")

    for each (string) in (finalized_list)
        (string_to_save_to_file) = (string_to_save_to_file)+(finalized_list(position(string))

    return (string_to_save_to_file) to main function
    """
    string_to_save_to_file = ""
    first_loop_counter = 0
    for list in finalized_list:
        finalized_list[first_loop_counter] = ("{},{},{},{}\n".format(list[0], list[1], list[2], list[3]))
        first_loop_counter += 1

    second_loop_counter = 0
    for i in finalized_list:
        string_to_save_to_file = string_to_save_to_file + finalized_list[second_loop_counter]
        second_loop_counter += 1
    return string_to_save_to_file


def print_items_list_all(printable_list, print_option):
    """
    :param printable_list:
    :param print_option:
    :return:
    """
    """Function to print all items/available items only/unavailable items only, in a specific format
    get (printable_list_of_lists) from main function.
    get (print_option) from main function

    counter_main = 0

    WORKING LIST REFERENCE
    working_list(0) = item name
    working_list(1) = item description
    working_list(2) = item price
    working_list(3) = item availability

    if (printing_selection) = print all
        for (items) in (printable_list_of_lists)
            (working_list) = (printable_list_of_Lists(position(counter_main)))

            (printing_spacing) = 40 - (length(working_list(position(0))+(working_list(position(1)))

            (blank_string) = (" " * (printing_spacing))

        check if (working_list(position(3))) = "in"
            print ["(counter_main)+" - "+(working_list(position(0))+(working_list(position(1))+blank_string+"=$ "+
            (working_list(position(2))"]

        else check if (working_list(position(3)) = "out"
            print ["(counter_main)+" - "+(working_list(position(0))+(working_list(position(1))+blank_string+"=$ "+
            (working_list(position(2))+"*""]

            (main_counter) = (main_counter) +1
            (blank_string) = " "

    if (printing_selection) = print unavailable only
        for (items) in (printable_list_of_lists)
            (working_list) = (printable_list_of_Lists(position(counter_main)))

            (printing_spacing) = 40 - (length(working_list(position(0))+(working_list(position(1)))

            (blank_string) = (" " * (printing_spacing))

        check if working_list(3) = "out"
            print ["(counter_main)+" - "+(working_list(position(0))+(working_list(position(1))+blank_string+"=$ "+
            (working_list(position(2))"]

            (main_counter) = (main_counter) +1
            (blank_string) = " "

    if printing_selection = print available only
        for (items) in (printable_list_of_lists)
            (working_list) = (printable_list_of_Lists(position(counter_main)))

            (printing_spacing) = 40 - (length(working_list(position(0))+(working_list(position(1)))

            (blank_string) = (" " * (printing_spacing))

        check if working_list(3) = "in"
            print ["(counter_main)+" - "+(working_list(position(0))+(working_list(position(1))+blank_string+"=$ "+
            (working_list(position(2))"]

            (main_counter) = (main_counter) +1
            (blank_string) = " "
"""
    counter_main = 0
    blank_string = ''

    ##print all items
    if print_option == 1:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'in':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            elif working_list[3] == 'out':
                print("{} - {} ({}){}\t\t\t= ${:.2f}{}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2]), '*'))

            counter_main += 1
            blank_string = ' '
    ##print only unavailable items
    elif print_option == 2:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'out':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            counter_main += 1
            blank_string = ' '
    ##print only available Items
    elif print_option == 3:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'in':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            counter_main += 1
            blank_string = ' '


def hire_item(list_of_items):
    """
    :param list_of_items:
    :return: new_list_of_items
    """
    """Function for Hiring an Item, error checks for inputs and modifies the list of items.
    get (list of items) from the main function
    (length_of_list) = length of (list_of_items)

    print to screen("Enter the number of an item to hire: ")
    (choice) = get user input

    ##This block of code checks the input to see if it is an integer type value
    Error check (choice) for integer type
    while (choice) is not integer type
        if (choice) is not integer type
            print to screen("Invalid input, enter a valid number")
            (choice) = get user input

    ##This block of code checks if the user choice is within the menu range, and checks if subsequent inputs = int type
    while ((choice) > length_of_list) or ((choice) < 0))
        print to screen("Invalid item number")
        (choice) = get user input
            Error check (choice) for integer type
            while (choice) is not integer type
                if (choice) is not integer type
                    print to screen("Invalid input, enter a valid number")
                    (choice) = get user input

    checked_item = list_of_items(choice)

    ##This block of code checks if the item selected is available for hire, checks input range and for input = int type
    while (checked_item(3)) does not = 'in'
        print to screen("That item is not available for hire.")

        Error check (choice) for integer type
        while (choice) is not integer type
            if (choice) is not integer type
                print to screen("Invalid input, enter a valid number")
                (choice) = get user input

        while ((choice) > length_of_list) or ((choice) < 0))
        print to screen("Invalid item number")
        (choice) = get user input
            Error check (choice) for integer type
            while (choice) is not integer type
                if (choice) is not integer type
                    print to screen("Invalid input, enter a valid number")
                    (choice) = get user input

            while ((choice) > length_of_list) or ((choice) < 0))
                print to screen("Invalid item number")
                (choice) = get user input
                Error check (choice) for integer type
                while (choice) is not integer type
                    if (choice) is not integer type
                        print to screen("Invalid input, enter a valid number")
                        (choice) = get user input

    checked_item = list_of_items(choice)

    item_name = checked_item(0)
    item_price = checked_item(2)

    print("{item_name} hired for ${item_price})

    checked_item(3) == "out"

    list_of_items(choice) = checked_item
    return list_of_items to Main function
    """
    new_list_of_items = list_of_items
    length_of_list = len(list_of_items)
    error_marker = 0
    while error_marker == 0:
        try:
            choice = int(input("Enter the number of an item to hire "))
            error_marker = 1
        except ValueError:
            print("Invalid input, enter a valid number")
            error_marker = 0

    while (choice > length_of_list) or (choice < 0):
        error_marker3 = 0
        while error_marker3 == 0:
            try:
                choice = int(input("Enter the number of an item to hire: "))
                error_marker3 = 1
            except ValueError:
                print("Invalid input; enter a number")
                error_marker3 = 0

    checked_item = list_of_items[choice]
    while (checked_item[3]) != 'in':
        print("That item is not available for hire")
        error_marker2 = 0
        while error_marker2 == 0:
            try:
                choice = int(input("Enter a valid number: "))
                error_marker2 = 1
            except ValueError:
                choice = input("Invalid input; enter a number")
                error_marker2 = 0

        while (choice > length_of_list) or (choice < 0):
            print("Invalid item number: ")
            error_marker4 = 0
            while error_marker4 == 0:
                try:
                    choice = int(input("Enter a valid number: "))
                    error_marker4 = 1
                except ValueError:
                    choice = input("Invalid input; enter a number")
                    error_marker4 = 0

        checked_item = list_of_items[choice]

    print("{} hired for ${}".format(checked_item[0], checked_item[2]))

    checked_item[3] = "out"

    new_list_of_items[choice] = checked_item
    return new_list_of_items


def return_item(list_of_items):
    """
    :param list_of_items:
    :return: new_items_list
    """
    """Function for returning an Item, error checks for inputs and modifies the list of items.
    get (list of items) from the main function
    (length_of_list) = length of (list_of_items)

    print to screen("Enter the number of an item to return: ")
    (choice) = get user input

    ##This block of code checks the input to see if it is an integer type value
    Error check (choice) for integer type
    while (choice) is not integer type
        if (choice) is not integer type
            print to screen("Invalid input, enter a valid number")
            (choice) = get user input

    ##This block of code checks if the user choice is within the menu range, and checks if subsequent inputs = int type
    while ((choice) > length_of_list) or ((choice) < 0))
        print to screen("Invalid item number")
        (choice) = get user input
            Error check (choice) for integer type
            while (choice) is not integer type
                if (choice) is not integer type
                    print to screen("Invalid input, enter a valid number")
                    (choice) = get user input

    checked_item = list_of_items(choice)

    ##This block of code checks if the item selected is available to return, checks input range and for input = int type
    while (checked_item(3)) does not = 'out'
        print to screen("That item is not on hire.")

        Error check (choice) for integer type
        while (choice) is not integer type
            if (choice) is not integer type
                print to screen("Invalid input, enter a valid number")
                (choice) = get user input

        while ((choice) > length_of_list) or ((choice) < 0))
        print to screen("Invalid item number")
        (choice) = get user input
            Error check (choice) for integer type
            while (choice) is not integer type
                if (choice) is not integer type
                    print to screen("Invalid input, enter a valid number")
                    (choice) = get user input

            while ((choice) > length_of_list) or ((choice) < 0))
                print to screen("Invalid item number")
                (choice) = get user input
                Error check (choice) for integer type
                while (choice) is not integer type
                    if (choice) is not integer type
                        print to screen("Invalid input, enter a valid number")
                        (choice) = get user input

    checked_item = list_of_items(choice)

    item_name = checked_item(0)
    item_price = checked_item(2)

    print("(item_name) returned)

    checked_item(3) == "in"

    list_of_items(choice) = checked_item
    return list_of_items to Main function
    """
    new_list_of_items = list_of_items
    length_of_list = len(list_of_items)
    error_marker = 0
    while error_marker == 0:
        try:
            choice = int(input("Enter the number of an item to return: "))
            error_marker = 1
        except ValueError:
            print("Invalid input; enter a number")
            error_marker = 0

    while (choice > length_of_list) or (choice < 0):
        error_marker3 = 0
        while error_marker3 == 0:
            try:
                choice = int(input("Invalid item number: "))
                error_marker3 = 1
            except ValueError:
                print("Invalid input, enter a valid number")
                error_marker3 = 0

    checked_item = list_of_items[choice]
    while (checked_item[3]) != 'out':
        print("That item is not on hire")
        error_marker2 = 0
        while error_marker2 == 0:
            try:
                choice = int(input("Enter a valid number: "))
                error_marker2 = 1
            except ValueError:
                choice = input("Invalid input; enter a number")
                error_marker2 = 0

        while (choice > length_of_list) or (choice < 0):
            print("Invalid item number: ")
            error_marker4 = 0
            while error_marker4 == 0:
                try:
                    choice = int(input("Enter a valid number: "))
                    error_marker4 = 1
                except ValueError:
                    choice = input("Invalid input; enter a number")
                    error_marker4 = 0

        checked_item = list_of_items[choice]

    print("{} returned".format(checked_item[0]))

    checked_item[3] = "in"

    new_list_of_items[choice] = checked_item
    return new_list_of_items


def add_new_item(list_of_items):
    """
    :param list_of_items:
    :return: amended_list_of_items
    """
    """Function to add a new item to the list of existing Items and error checks inputs.
    get (list_of_items) from main function
    (amended_list_of_items) = (list_of_items)

    print to screen("please enter item name: ")
    (new_item_name) = user input
    Error check to see if user input is blank
    while user input is blank
        if user input is blank
        print to screen("item name cannot be blank")
        (new_item_name) = user input

    print to screen("please enter item description: ")
    (new_item_description) = user input
    Error check to see if user input is blank
    while user input is blank
        if user input is blank
        print to screen("item name cannot be blank")
        (new_item_description) = user input

    print to screen("please enter item price")
    (new_item_price) = user input
    Error check for Valid float type and if user input is blank
    while user input is blank/not float type
        if user input is blank/not float type
            print to screen("invalid input")
            (new_item_price) = user input

    set (new_item_availability) = 'in'
    (new_item_list) = [(new_item_name), (new_item_description), (new_item_price), (new_item_availability)]
    add (new_item_list) to (amended_list_of_items)

    return (amended_list_of_items) to main function
    """
    amended_list_of_items = list_of_items

    new_item_name = input("Item name ")
    while new_item_name == "":
        new_item_name = input("Input cannot be blank ")

    new_item_description = input("Description ")
    while new_item_description == "":
        new_item_description = input("Input cannot be blank ")

    error_marker = 0
    while error_marker == 0:
        try:
            new_item_price = float(input("Price per day "))
            error_marker = 1
        except ValueError:
            print("Invalid input, enter a valid number")
            error_marker = 0

        if new_item_price < 0:
            print("Price must be >= $0")
            error_marker = 0

    new_item_availability = "in"

    new_item_list = []
    new_item_list.append(new_item_name)
    new_item_list.append(new_item_description)
    new_item_list.append(new_item_price)
    new_item_list.append(new_item_availability)

    amended_list_of_items.append(new_item_list)
    print("{} {}, {:.2f} now available for hire".format(new_item_name, new_item_description, new_item_price))
    return amended_list_of_items


def check_item_status(items_list_to_check_availability, in_or_out_string):
    """
    :param items_list_to_check_availability:
    :param in_or_out_string:
    :return: list_check_boolean
    """
    """Function to check if any items are either 'in' or 'out' and return a boolean 1 if this is the case, 0 if not
    get (items_list_to_check_availability) from main function
    get (chosen_string) to check from main function, ['in' or 'out']
    list_check_boolean = 0

    for each item in items_list_to_check_availability
        check if (chosen_string) = (item_list(position(3))
        if chosen_string = (item_list(position(3))
            list_check_boolean = 1

    return (list_check_boolean) to main function

    ##Authors Note: I attempted to use the Python inbuilt functions all() and any() by generating a list of the logical
    [3] position in each item, which would give me a list of strings which were either 'in' or 'out' and then checking
    them with any() or all() but somehow the boolean values were not resolving the way i understood they should.
    This part of the code could be greatly simplified if i could get those functions to work.

    """
    counter = 0
    list_check_boolean = 0
    for i in items_list_to_check_availability:
        working_list = items_list_to_check_availability[counter]
        if working_list[3] == in_or_out_string:
            list_check_boolean = 1

        counter += 1

    return(list_check_boolean)


#main(FILE_NAME)