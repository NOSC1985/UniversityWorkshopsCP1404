"""
Author: Nicholas Stanton-Cook
Dates: 12/5/2016 -> 22/5/2016

Description: This program allows a user to check and manage a list of items for sale, stored and retrieved from a
C.S.V formatted text file. The user is presented with a GUI allowing them choices to check the status of all items,
hire out an item, return an item, add a new item and confirm their choice.

Also included are pop up windows for inputs when  Adding new items
(This will use an error checking to ensure valid inputs)

git hub repository: https://github.com/NOSC1985/UniversityWorkshopsCP1404/tree/
5b7507b08c9e89c63611b6c88dddfb8c3c951371/Assignment2

Referenced material and studied various files from the Kivy Demos Provided
https://github.com/CP1404/KivyDemos
"""
from Item import *
from ItemList import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemsForHire import format_csv_file_data_for_use
from itemsForHire import format_csv_file_data_to_save


__Author__ = "Nicholas Stanton-Cook"
FILE_NAME = "items.csv"

import_file = open("{}".format(FILE_NAME), mode='r')
items_lists = format_csv_file_data_for_use(import_file)
import_file.close()

"""
making a list of Item objects and creating an ItemList class object
"""
list_of_item_objects = []
counter = 0
for item in items_lists:
    current_item_name = item[0]
    current_item_description = item[1]
    current_item_price = item[2]
    current_item_availability = item[3]
    current_item = Item(current_item_name, current_item_description, current_item_price, current_item_availability)
    list_of_item_objects.append(current_item)

    item_list_object = ItemList(list_of_item_objects)


def convert_item_list_to_dictionary(list_of_items):
    """
    Function: convert_item_list_to_dictionary
    :param list_of_items:
    :return: dictionary_of_items
    """
    dictionary_of_items = {}
    for items in list_of_items:
        item_name = items[0]
        item_details = [items[1], items[2], items[3]]
        dictionary_of_items[item_name] = item_details

    return dictionary_of_items


def convert_item_dictionary_to_list(item_dictionary):
    """
    Function: convert_item_dictionary_to_list
    :param item_dictionary:
    :return: list_of_items
    """
    list_of_items = []
    item_names = item_dictionary.keys()
    for each_item in item_names:
        item_name = [each_item]
        item_description = item_dictionary[each_item]
        working_item = [item_name + item_description]
        list_of_items = list_of_items + working_item

    return list_of_items


class ItemsForHireApp(App):
    """
    Program: ItemsForHire(App)
    This program controls the creation and function of all the GUI objects including the functionality of each
    button or text input.
    Includes Error checking for correct input format and type.
    """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        Allocate the following properties
        items_dict (allows the current set of items to be stored centrally and accessed by all functions)
        mode (allows the program to detect if it is currently in List, Hire or Return Mode and act accordingly)
        hiring_list (allows the list of names of items which have been selected to be stored and accessed centrally)
        total_hiring_price (contains the current hiring price of the items currently selected)
        items_to_display_string (contains the current constructed string of items to display to the screen)
        returning_list (allows the list of names of items which have been selected to be stored and accessed centrally)
        """
        super(ItemsForHireApp, self).__init__(**kwargs)
        self.item_list_object = item_list_object
        self.items_dict = convert_item_list_to_dictionary(items_lists)
        self.mode = 0
        self.hiring_list = []
        self.total_hiring_price = 0
        self.items_to_display_string = ""
        self.returning_list = []

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Items For Hire"
        self.root = Builder.load_file('items_for_hire_two.kv')
        self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        """
        for each name in items_dict
            create Button with text(current_name)
            set Button to run press_entry function on release
            set Button to run clear_all on press
            generate a widget for the Button
            find the current items data from items_dict
            if working_item(availability) = 'in'
                make Button colour Green
            else if working_item(availability) = 'out'
                make Button colour Red

            make sure that the buttons separate into columns of maximum 5
        """
        build_list = self.item_list_object.get_whole_list()
        for name in build_list:
            temp_button = Button(text=name.name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.bind(on_press=self.clear_all)
            self.root.ids.entriesBox.add_widget(temp_button)

            if name.availability == 'in':
                temp_button.background_color = (0, 1, 0, 1)
            elif name.availability == 'out':
                temp_button.background_color = (1, 0, 0, 1)
            self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1

    def press_entry(self, instance):
        """
        Handler for pressing the currently stored item buttons
        :param instance: Whichever button was pressed to activate this callback
        :return: None
        """
        """
        get all details about the current buttons item from items_dict

        if current program Mode = 0 (listing Items)
            display only Items name and details to the status bar

        else if current program Mode = 1 (Hiring Items)
            if current item is available for hire
                if current item has not already been selected
                    add item to the list of items to hire
                    add items price to the total current hire price

                reset the display string
                re-make the display string to include all items currently in the list of items to hire

                print the new formatted list of Items selected for hire to the status bar

        else if current program Mode = 2 (Return Items)
            if current item is out on hire
                if current item has not already been selected
                    add item to the list of items to return

                reset the display string
                re-make the display string to include all items currently in the list of items to return

                print the new formatted list of Items selected for return to the status bar
        """
        name = instance.text
        item_object = self.item_list_object.get_specific_item(name)
        #details = self.items_dict[name]
        #description = details[0]
        #price = details[1]
        #availability = details[2]

        if self.mode == 0:
            self.status_text = "'{}': {} \nPrice: ${}\nAvailability: {}".format(item_object.name,
                                                                                item_object.description,
                                                                                item_object.price,
                                                                                item_object.availability)

        elif self.mode == 1:
            if item_object.availability == 'in':
                if item_object.name not in self.hiring_list:
                    self.hiring_list.append(name)
                    self.total_hiring_price += float(item_object.price)
                self.items_to_display_string = ""
                for items in self.hiring_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Hire\n{}\nPrice: {}".format(self.items_to_display_string,
                                                                         str(self.total_hiring_price))

        elif self.mode == 2:
            if item_object.availability == 'out':
                if item_object.name not in self.returning_list:
                    self.returning_list.append(name)

                self.items_to_display_string = ""
                for items in self.returning_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Return\n{}".format(self.items_to_display_string)

        instance.state = 'down'

    def press_clear(self):
        """
        Handler for pressing the Clear Button
        returns all data to first states and resets the widget to first state
        :return: None
        """
        """
        reset all buttons in main widget to normal
        status_text = blank string
        hiring_list = blank list
        hiring_price = 0
        items_to_display_string = blank string
        returning_list = blank list
        """
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""
        self.hiring_list = []
        self.total_hiring_price = 0
        self.items_to_display_string = ""
        self.returning_list = []


    def clear_all(self, instance):
        """
        Function to reset only the Buttons on the widget to their normal states but not reset the data stored.
        This allows us to have only one button selected at a time.
        :return: None
        """
        for instance in self.root.ids.entriesBox.children:
            if instance.state == 'down':
                instance.state = 'normal'

    def press_list_items(self):
        """
        Handler for pressing the list_items button
        clears the date from Hiring/Returning Items and sets the program to Mode 0 (listing items)
        :return: None
        """
        self.press_clear()
        self.mode = 0
        print(self.mode)

    def press_hire_item(self):
        """
        Handler for pressing the hire_item button
        displays instructions about how to hire items and sets the program Mode to 1 (Hire Items)
        :return: None
        """
        self.status_text = "Select Items to Hire Above\nPress 'Confirm' when ready to hire\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 1
        print(self.mode)

    def press_return_item(self):
        """
        Handler for pressing the return_item button
        displays instructions about how to return items and sets the program Mode to 2 (return Items)
        :return: None
        """
        self.status_text = "Select Items to Return Above\nPress 'Confirm' when ready to Return\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 2
        print(self.mode)

    def press_new_item(self):
        """
        Handler for pressing the add_new_item button
        Opens the popup widget to allow for data entry
        :return: None
        """
        self.status_text = "Enter details for the new Item"
        self.root.ids.popup_for_new_item.open()

    def press_save_new_item(self, new_item_name, new_item_description, new_item_price):
        """
        Handler for pressing the save button in the add entry popup
        :param new_item_name: name from text input (from popup GUI)
        :param new_item_description: description from text input (from popup GUI)
        :param new_item_price: price price from text input (from popup GUI)
        :return: None
        """
        """
        Error Check new_item_name for blank string
        Error Check new_item_description for blank string
        Error check new_item_price for numerical float type input
        Error check new_item_price for positive number (input > = 0) input

        create Button with text(new_item_name)
        set Button to run press_entry function on release
        set Button to run clear_all on press
        generate a widget for the Button
        new_item(availability = 'in')
        make Button colour Green
        make sure that the buttons separate into columns of maximum 5

        clear popup entry data
        close popup
        """
        error_marker = 0
        try:
            new_item_price = new_item_price.strip('$')
            check_price = float(new_item_price)

            if check_price < 0:
                error_marker = 1
                new_item_price = "error"
                check_price = float(new_item_price)

            if new_item_name == "":
                error_marker = 2
                new_item_price = "error"
                check_price = float(new_item_price)

            if new_item_description == "":
                error_marker = 3
                new_item_price = "error"
                check_price = float(new_item_price)

            self.items_dict[new_item_name] = [new_item_description, new_item_price, "in"]
            self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1
            temp_button = Button(text=new_item_name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.bind(on_press=self.clear_all)
            self.root.ids.entriesBox.add_widget(temp_button)
            temp_button.background_color = (0, 1, 0, 1)
            self.root.ids.popup_for_new_item.dismiss()
            self.clear_fields()
            self.status_text = ""

        except ValueError:
            if error_marker == 0:
                self.status_text = "Incorrect Input: Please Enter a Number"
                self.root.ids.new_item_price.value = ""
                self.root.ids.new_item_price.text = ""
            elif error_marker == 1:
                self.status_text = "Incorrect Input: Price must not be Negative"
                self.root.ids.new_item_price.value = ""
                self.root.ids.new_item_price.text = ""
            elif error_marker == 2:
                self.status_text = "Incorrect Input: Name Cannot Be Blank"

            elif error_marker == 3:
                self.status_text = "Incorrect Input: Description Cannot Be Blank"

            error_marker = 0

    def press_confirm_item(self):
        """
        Handler for pressing the confirm button
        Confirms that the user will Hire/Return the currently selected Items
        """
        """
        if current program Mode = 0
            do nothing

        else if current program Mode = 1 (hire Items)
            for each item in hiring_list
                update items_dict availability = 'out'

            for each Button name in hiring_list
                change button colour to Red

            final_price = total_hiring_price
            generate final message to display all items just hired

        else if current program Mode = 2 (return Items)
            for each item in returning_list
                update items_dict availability = 'in'

            for each Button name in hiring_list
                change button colour to Green

            generate final message to display all items just Returned

        change current program Mode to 0 (list items)
        run press_clear()
        display final_message to status bar

        """
        final_message = ""
        if self.mode == 1:
            for i in self.items_dict:
                check_current_item = self.items_dict[i]
                if i in self.hiring_list:
                    check_current_item[2] = 'out'
                    self.items_dict[i] = check_current_item

            for instance in self.root.ids.entriesBox.children:
                print(instance.text)
                if instance.text in self.hiring_list:
                    instance.background_color = (1, 0, 0, 1)

            final_price = float(self.total_hiring_price)
            final_message = "{}\n Hired for: ${}".format(self.items_to_display_string, final_price)

        elif self.mode == 2:
            for i in self.items_dict:
                check_current_item = self.items_dict[i]
                if i in self.returning_list:
                    check_current_item[2] = 'in'
                    self.items_dict[i] = check_current_item

            for instance in self.root.ids.entriesBox.children:
                print(instance.text)
                if instance.text in self.returning_list:
                    instance.background_color = (0, 1, 0, 1)
            final_message = "{}\n returned".format(self.items_to_display_string)

        self.mode = 0
        self.press_clear()
        self.status_text = "{}".format(final_message)

    def press_save(self):
        """
        Handler for pressing the save button
        calls the functions needed to format the date and saves it to file
        :return: None
        """
        final_list = convert_item_dictionary_to_list(self.items_dict)
        save_file_data = format_csv_file_data_to_save(final_list)
        save_file = open("{}".format(FILE_NAME), mode='w')
        save_file.write(save_file_data)
        save_file.close()
        final_item_count = len(final_list)
        self.status_text = "{} items saved to {}".format(final_item_count, FILE_NAME)

    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        Clears the fields in the popup window entries
        :return: None
        """
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_description.text = ""
        self.root.ids.new_item_price.text = ""

    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        clears the popup fields and closes the popup
        :return: None
        """
        self.root.ids.popup_for_new_item.dismiss()
        self.clear_fields()
        self.status_text = ""

    def on_stop(self):
        """
        function to save data to file on close
        calls the functions needed to format the date and saves it to file
        :return: None
        """
        final_list = convert_item_dictionary_to_list(self.items_dict)
        save_file_data = format_csv_file_data_to_save(final_list)
        save_file = open("{}".format(FILE_NAME), mode='w')
        save_file.write(save_file_data)
        save_file.close()
        final_item_count = len(final_list)
        self.status_text = "{} items saved to {}\nHave a nice day :)".format(final_item_count, FILE_NAME)

ItemsForHireApp().run()
