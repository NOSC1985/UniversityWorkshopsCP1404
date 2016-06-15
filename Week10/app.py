from kivy.app import App
from kivy.lang import Builder

from Game import Game


class ErrorOutsideLimit(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class GuessingGame(App):
    def __init__(self):
        super(GuessingGame, self).__init__()
        self.game = Game()

    def build(self):
        self.title = "Guessing Game 0.0.1"
        self.root = Builder.load_file('gui.kv')
        self.root.size = (300, 500)
        print(type(self.root.ids))
        return self.root

    def handle_new_game(self):
        self.game = Game()

    def handle_guess(self):
        user_guess = self.root.ids.guess_input.text
        try:
            user_guess = int(user_guess)
            if 0 <= user_guess <= 10:
                self.root.ids.game_info_text.text = "{}".format(self.game.guess(user_guess))
                self.root.ids.game_guess_number.text = "Guess Number = {}".format(self.game.add_move())
            else:
                raise ErrorOutsideLimit("stoopid")

        except (ValueError, TypeError, ErrorOutsideLimit):
            self.root.ids.game_info_text.text = "please enter a number between 1 and 10"
            print("please enter a number between 1 and 10")

    def handle_menu(self, current_menu):
        normal = [1, 1, 1, 1]
        hilight = [0, 0, 1, 1]

        menu_context_list = ['settings_screen', 'about_screen', 'game_screen']

        for key in self.root.ids:
            if key in menu_context_list:
                if key == current_menu:
                    self.root.ids[key].background_color = hilight
                else:
                    self.root.ids[key].background_color = normal


# create and start the App running
GuessingGame().run()