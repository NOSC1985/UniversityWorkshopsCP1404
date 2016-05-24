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


def convert_item_list_to_dictionary(list_of_items):
    dictionary_of_items = {}
    for item in list_of_items:
        item_name = item[0]
        item_details = [item[1], item[2], item[3]]
        dictionary_of_items[item_name] = item_details

    print(dictionary_of_items)
    return dictionary_of_items


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
        # basic data example - dictionary of names: phone numbers
        self.items_dict = convert_item_list_to_dictionary(items_lists)

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
        self.status_text = "'{}': {} Price: ${}".format(name, description, price)
        instance.state = 'down'

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""

    def clear_all(self, instance):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""

    def press_list_items(self):
        """
        Handler for pressing the list_items button
        :return: None
        """

    def press_hire_item(self):
        """
        Handler for pressing the hire_item button
        :return: None
        """

    def press_return_item(self):
        """
        Handler for pressing the return_item button
        :return: None
        """

    def press_new_item(self):
        """
        Handler for pressing the add_new_item button
        :return: None
        """
        self.status_text = "Enter details for the new Item"
        # this opens the popup
        self.root.ids.popup_for_new_item.open()

    def press_confirm_item(self, added_name, added_number):
        """
        Handler for pressing the confirm button
        :return: None
        """


    def press_save(self, new_item_name, new_item_description, new_item_price):
        """
        Handler for pressing the save button
        :return: None
        """

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


ItemsForHireApp().run()
