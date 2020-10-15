from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

import math


class Gui(GridLayout):
    # blue
    default_color_1 = (0, 1, 255, 1)
    # grey
    default_color_2 = (1, 1, 1, 1)

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 9

        self.spacing = [20, 20]

        labels = [
                "Navn:",
                "Adresse:",
                "PostAdr:",
                "Antall:",
                "Pris:",
                "Bilde:",
                "Detaljer:"
        ]

        # back_layout = FloatLayout(size=(300, 300))



        for label in labels:
            label = Label(text=label)
            textinput = TextInput(text='Hello world', multiline=True)


            self.add_widget(label)
            self.add_widget(textinput)

        # spot = Button(text=str("Hi change!"))
        # spot.defaultColor = Gui.default_color_1

        # self.add_widget(spot)
