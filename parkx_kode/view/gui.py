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

        self.layout = GridLayout()

        spot = Button(text=str("Hi change!"))
        spot.defaultColor = Gui.default_color_1

        self.add_widget(spot)
