"""
Author: Nicholas Stanton-Cook
Dates: 12/5/2016 -> 22/5/2016

Description: This program allows a user to check and manage a list of items for sale, stored and retrieved from a
C.S.V formatted text file. The user is presented with a GUI allowing them choices to diplay all items,
hire out an item, return an item, add a new item and confirm their choice.

Also included are pop up windows for inputs when  Adding new items
(This will use an error checking to ensure valid inputs)

git hub repository: https://github.com/NOSC1985/UniversityWorkshopsCP1404/tree/
5b7507b08c9e89c63611b6c88dddfb8c3c951371/Assignment2

Referenced material and studied various files from the Kivy Demos Provided
https://github.com/CP1404/KivyDemos
"""
from Item import *
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


list_of_item_objects = []
counter = 0
for item in items_lists:
    current_item_name = item[0]
    current_item_description = item[1]
    current_item_price = item[2]
    current_item_availability = item[3]
    current_item = Item(current_item_name, current_item_description, current_item_price, current_item_availability)
    list_of_item_objects.append(current_item)
    counter += 1

#for item in list_of_item_objects:
    #item_to_check = item.name
    #print(item_to_check)


def convert_item_list_to_dictionary(list_of_items):
    dictionary_of_items = {}
    for items in list_of_items:
        item_name = items[0]
        item_details = [items[1], items[2], items[3]]
        dictionary_of_items[item_name] = item_details

    return dictionary_of_items


def convert_item_dictionary_to_list(item_dictionary):
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
        """
        super(ItemsForHireApp, self).__init__(**kwargs)
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
        for name in self.items_dict:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.bind(on_press=self.clear_all)
            self.root.ids.entriesBox.add_widget(temp_button)
            working_item = self.items_dict[name]
            if working_item[2] == 'in':
                temp_button.background_color = (0, 1, 0, 1)
            elif working_item[2] == 'out':
                temp_button.background_color = (1, 0, 0, 1)
            self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1

    def press_entry(self, instance):
        """
        Handler for pressing the currently stored item buttons
        :param instance: the Kivy button instance
        :return: None
        """
        name = instance.text
        details = self.items_dict[name]
        description = details[0]
        price = details[1]
        availability = details[2]

        if self.mode == 0:
            self.status_text = "'{}': {} \nPrice: ${}\nAvailability: {}".format(name, description, price, availability)

        elif self.mode == 1:
            if availability == 'in':
                if name not in self.hiring_list:
                    self.hiring_list.append(name)
                    self.total_hiring_price += float(price)
                self.items_to_display_string = ""
                for items in self.hiring_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Hire\n{}\nPrice: {}".format(self.items_to_display_string,
                                                                         str(self.total_hiring_price))

        elif self.mode == 2:
            if availability == 'out':
                if name not in self.returning_list:
                    self.returning_list.append(name)

                self.items_to_display_string = ""
                for items in self.returning_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Return\n{}".format(self.items_to_display_string)

        instance.state = 'down'

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
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
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        for instance in self.root.ids.entriesBox.children:
            if instance.state == 'down':
                instance.state = 'normal'

    def press_list_items(self):
        """
        Handler for pressing the list_items button
        :return: None
        """
        App.press_clear(self)
        self.mode = 0

    def press_hire_item(self):
        """
        Handler for pressing the hire_item button
        :return: None
        """
        self.status_text = "Select Items to Hire Above\nPress 'Confirm' when ready to hire\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 1

    def press_return_item(self):
        """
        Handler for pressing the return_item button
        :return: None
        """
        self.status_text = "Select Items to Return Above\nPress 'Confirm' when ready to Return\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 2

    def press_new_item(self):
        """
        Handler for pressing the add_new_item button
        :return: None
        """
        self.status_text = "Enter details for the new Item"
        self.root.ids.popup_for_new_item.open()

    def press_save_new_item(self, new_item_name, new_item_description, new_item_price):
        """
        Handler for pressing the save button in the add entry popup - save a new entry to memory
        :param new_item_name: name text input (from popup GUI)
        :param added_number: phone number text input (string)
        :return: None
        """
        new_item_price = new_item_price.strip('$')
        self.items_dict[new_item_name] = [new_item_description, new_item_price, "in"]
        self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1
        temp_button = Button(text=new_item_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        temp_button.background_color = (0, 1, 0, 1)
        self.root.ids.popup_for_new_item.dismiss()
        self.clear_fields()

    def press_confirm_item(self, added_name, added_number):
        """
        Handler for pressing the confirm button

        """

    def press_save(self):
        """
        Handler for pressing the save button
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
        If we don't do this, the popup will still have text in it when opened again
        :return: None
        """
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_description.text = ""
        self.root.ids.new_item_price.text = ""

    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        :return: None
        """
        self.root.ids.popup_for_new_item.dismiss()
        self.clear_fields()
        self.status_text = ""

    def on_stop(self):
        """
        Handler for pressing the save button
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
