from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import math



class Gui(GridLayout):

    # blue
    default_color_1 = (0, 1, 255, 1)
    # grey
    default_color_2 = (1, 1, 1, 1)

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.sudoku_board = GridLayout()

        spot = Button(text=str("Hello there Guys!"))
        spot.defaultColor = Gui.default_color_1

        # self.sudoku_board.add_widget(spot)

        self.add_widget(spot)

