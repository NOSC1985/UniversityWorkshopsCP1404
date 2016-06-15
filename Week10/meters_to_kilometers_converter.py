"""
Author: Nicholas Stanton-Cook
Dates: 14/5/2016 -> 17/5/2016
Description: This program ant the accompanying Kivy file, generate a GUI which allows the user to enter a float style
input into a text input area, raise or lower the value they have entered by 0.1 by pressing the available "up" and
"down" buttons on the GUI, and by pressing the "Conversion" Button, allow them to receive useful approximations of the
entered value converted to Kilometers
"""
__Author__ = "Nicholas Stanton-Cook"

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '150')
"""
change these values to change the value that the up/down buttons
will scale by
"""
SCALING_FOR_UP_AND_DOWN_BUTTONS = 0.1


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Meters to Kilometers Conversion Program"
        self.root = Builder.load_file('meters_to_kilometers.kv')
        return self.root

    def handle_conversion(self):
        """
        handle_conversion()
        This function will handle the code which will execute when the "Conversion" button is pressed in the GUI
        converts the current value of the User input from meters to Kilometers and provides simple display error
        checking
        """
        """
        get current value of user_input as a float type
        convert the current value from Meters to Kilometers

        if converted_value < decimal place threshold
            print message that input is under the threshold of the program

        else
            display the value correctly formatted to output_screen
        """
        current_user_entered_value = float(self.root.ids.user_input.text)
        converted_value = current_user_entered_value / 1000
        if converted_value < 0.01:
            self.root.ids.output_screen.text = "Less than 0.01km"

        else:
            self.root.ids.output_screen.text = "Approximately {:.2f}km".format(converted_value)

    def handle_up(self):
        """
        handle_up()
        This function will handle the execution of the code required when the "Up" button is pressed on the GUI
        Converts and increases the number entered into the user_input before changing the value displayed in
        user_input to reflect the new increased value.
        Provides error checking for blank and non numerical inputs.
        Provides and enforces limitations on the display formatting.
        """
        """
        Error Check the user_input value for correct type "float"
        Error check for no input entered
        if error
            clear user_input text
            display error message in output_screen

        get current value from user_input as float type
        new_value = current_value + SCALING_FOR_UP_AND_DOWN_BUTTONS
        user_input text = new_value formatted to correct decimal places
        """
        try:
            input_string = self.root.ids.user_input.text
            float_number_value = float(input_string)
            new_display_value = float_number_value + SCALING_FOR_UP_AND_DOWN_BUTTONS
            self.root.ids.user_input.text = "{:.2f}".format(new_display_value)

        except ValueError:
            self.root.ids.user_input.text = ''
            self.root.ids.output_screen.text = "Error, please enter a number."

    def handle_down(self):
        """
        handle_down()
        This function will handle the execution of the code required when the "Down" button is pressed on the GUI
        Converts and decreases the number entered into the user_input before changing the value displayed in
        user_input to reflect the new increased value.
        Provides error checking for blank and non numerical inputs.
        Provides and enforces limitations on the display formatting.
        """
        """
        Error Check the user_input value for correct type "float"
        Error check for no input entered
        if error
            clear user_input text
            display error message in output_screen

        get current value from user_input as float type
        new_value = current_value - SCALING_FOR_UP_AND_DOWN_BUTTONS
        user_input text = new_value formatted to correct decimal places
        """
        try:
            input_string = self.root.ids.user_input.text
            float_number_value = float(input_string)
            new_display_value = float_number_value - SCALING_FOR_UP_AND_DOWN_BUTTONS
            self.root.ids.user_input.text = "{:.2f}".format(new_display_value)

        except ValueError:
            self.root.ids.user_input.text = ''
            self.root.ids.output_screen.text = "Error, please enter a number."

BoxLayoutDemo().run()
