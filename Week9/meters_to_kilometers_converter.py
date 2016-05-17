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
        self.root.ids.output_screen.text = "Hello {}".format(self.root.ids.user_input.text)

    def handle_up(self):
        self.root.ids.output_screen.text = ''
        self.root.ids.user_input.text = ''

    def handle_down(self):
        self.root.ids.output_screen.text = ''
        self.root.ids.user_input.text = ''

BoxLayoutDemo().run()