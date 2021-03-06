from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '200')


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_screen.text = "Hello {}".format(self.root.ids.user_input.text)

    def handle_clear(self):
        self.root.ids.output_screen.text = ''
        self.root.ids.user_input.text = ''

BoxLayoutDemo().run()
