from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


class TaxiSimulator(App):
    def build(self):
        self.title = "Taxi Simulator"
        self.root = Builder.load_file('taxi_simulator.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_screen.text = "Hello {}".format(self.root.ids.user_input.text)

    def handle_clear(self):
        self.root.ids.output_screen.text = ''
        self.root.ids.user_input.text = ''

TaxiSimulator().run()
