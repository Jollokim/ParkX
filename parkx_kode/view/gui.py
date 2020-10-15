from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

import math


class Gui(BoxLayout):

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)
        self.orientation = "vertical"

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

        back_button = Button(text='Avbryt', size=(100, 40), size_hint=(None, None))
        self.add_widget(back_button)

        self.grid_scheme = GridLayout(cols=2, rows=7)
        self.add_widget(self.grid_scheme)

        self.text_fields = []

        for label in labels:
            label = Label(text=label)
            text_input = TextInput(text='Hello world', multiline=True)

            self.text_fields.append(text_input)

            self.grid_scheme.add_widget(label)
            self.grid_scheme.add_widget(text_input)

        insert_button = Button(text='Legg til', size=(100, 40), size_hint=(None, None))
        insert_button.bind(on_press=self.get_input_data)
        self.add_widget(insert_button)



    def get_input_data(self, instance):
        print(self.text_fields[0].text)
        self.text_fields[1].text = "Clicked a button did ya?!"

    def _clear_scene(self):
        self.clear_widgets()
