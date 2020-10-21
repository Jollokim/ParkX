from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconLayout


class Gui(BoxLayout):
    FIELDS = [
        "Navn:",
        "Adresse:",
        "PostAdr:",
        "Antall:",
        "Pris:",
        "Bilde:",
        "Detaljer:"
    ]

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.controller = None

        self.text_fields = []
        # self.create_legg_til_PP_scene()
        self.SCENES = [
            self._create_my_PPs_scene,
            self._create_legg_til_PP_scene
        ]

        self.SCENES[0]()

    def _create_legg_til_PP_scene(self):
        self.orientation = "vertical"

        self.spacing = [20, 20]

        back_button = Button(text='Avbryt', size=(100, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(0))
        self.add_widget(back_button)

        grid_scheme = GridLayout(cols=2, rows=7)
        self.add_widget(grid_scheme)

        for label in Gui.FIELDS:
            label = Label(text=label)
            text_input = TextInput(text='', multiline=True)

            self.text_fields.append(text_input)

            grid_scheme.add_widget(label)
            grid_scheme.add_widget(text_input)

        insert_pp_button = Button(text='Legg til', size=(100, 40), size_hint=(None, None))
        insert_pp_button.bind(on_press=self.insert_pp_button_handler)
        self.add_widget(insert_pp_button)

    def insert_pp_button_handler(self, instance):
        data_list = []
        for field in self.text_fields:
            data_list.append(field.text)

        self.controller.addNewParkingPlace(data_list)


    def print_input_data(self):
        for i in range(len(self.text_fields)):
            print(f"{Gui.FIELDS[i]} {self.text_fields[i].text}")

    def _clear_scene(self):
        self.clear_widgets()

    def switch_scene(self, n_scene):
        self._clear_scene()
        self.SCENES[n_scene]()

    def _create_my_PPs_scene(self):
        self.orientation = "vertical"

        self.spacing = [20, 20]

        button_box = BoxLayout(orientation="horizontal", spacing=0)
        self.add_widget(button_box)

        back_button = Button(text='Avbryt', size=(100, 40), size_hint=(.1, 0), pos_hint={"top": 1})
        back_button.bind(on_press=lambda instance: None)
        button_box.add_widget(back_button)

        go_leggInn_button = Button(text='Legg til parkeringsplass', size=(100, 40), size_hint=(.1, 0), pos_hint={"top": 1})
        go_leggInn_button.bind(on_press=lambda instance: self.switch_scene(1))

        button_box.add_widget(go_leggInn_button)

        # PPs_list = self.controller.getPPs



        grid_scheme = GridLayout(cols=1, rows=8)
        self.add_widget(grid_scheme)






