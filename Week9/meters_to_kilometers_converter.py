from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '150')

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Meters to Kilometers Conversion Program"
        self.root = Builder.load_file('meters_to_kilometers.kv')
        return self.root

    def handle_conversion(self):
        current_user_entered_value = float(self.root.ids.user_input.text)
        converted_value = current_user_entered_value / 1000
        if converted_value < 0.01:
            self.root.ids.output_screen.text = "Less than 0.01km"

        else:
            self.root.ids.output_screen.text = "Approximately {:.2f}km".format(converted_value)

    def handle_up(self):
        try:
            input_string = self.root.ids.user_input.text
            float_number_value = float(input_string)
            new_display_value = float_number_value + 0.1
            self.root.ids.user_input.text = "{:.2f}".format(new_display_value)

        except ValueError:
            self.root.ids.user_input.text = ''
            self.root.ids.output_screen.text = "Error, please enter a number."

    def handle_down(self):
        try:
            input_string = self.root.ids.user_input.text
            float_number_value = float(input_string)
            new_display_value = float_number_value - 0.1
            self.root.ids.user_input.text = "{:.2f}".format(new_display_value)

        except ValueError:
            self.root.ids.user_input.text = ''
            self.root.ids.output_screen.text = "Error, please enter a number."

BoxLayoutDemo().run()
