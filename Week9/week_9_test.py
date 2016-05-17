from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '1000')

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Test"
        self.root = Builder.load_file('Test.kv')
        return self.root

BoxLayoutDemo().run()
