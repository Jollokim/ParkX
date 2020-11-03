from functools import partial

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage


class Gui(BoxLayout):
    FIELDS = [
        "Navn",
        "Adresse",
        "PostAdr",
        "Antall",
        "Pris",
        "Bilde",
        "Detaljer"
    ]

    def __init__(self, controller,  **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.controller = controller

        self.PPs_list = controller.get_all_pp_from_list()
        self.controller.addPlaceholderPlaces()

        self.text_fields = []

        self.SCENES = [
            self._create_my_PPs_scene,
            self._create_legg_til_PP_scene,
            self._create_detailedPP_owner_scene,
            self._create_detailedPP_renter_scene,
            self._show_available_and_active_parkings_scene,
            self._main_menu_scene,
            self._my_profile_scene
        ]

        self.SCENES[5]()

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
        data_dict = {}

        for i in range(len(self.text_fields)):
            data_dict[Gui.FIELDS[i]] = self.text_fields[i].text

        self.controller.add_parking_place_to_repo(data_dict)

    def _clear_scene(self):
        self.clear_widgets()

    def switch_scene(self, n_scene):
        self._clear_scene()
        self.SCENES[n_scene]()

    def _create_my_PPs_scene(self):
        self.orientation = "vertical"

        self.spacing = [20, 20]

        button_box = BoxLayout(orientation="horizontal", spacing=0, size_hint=(1, 0.1))
        self.add_widget(button_box)

        back_button = Button(text='Main Menu', size=(100, 40), size_hint=(.1, 0), pos_hint={"top": 1})
        back_button.bind(on_press=lambda instance: self.switch_scene(5))
        button_box.add_widget(back_button)

        go_leggInn_button = Button(text='Legg til parkeringsplass', size=(100, 40), size_hint=(.1, 0),
                                   pos_hint={"top": 1})
        go_leggInn_button.bind(on_press=lambda instance: self.switch_scene(1))

        button_box.add_widget(go_leggInn_button)

        grid_scheme = GridLayout(cols=1, rows=8)
        self.add_widget(grid_scheme)

        # PPs_list = self.controller.getPPs

        PPs_list = [
            {"name": "Den store PP", "status": "I bruk", "bilde": "pp.jpg"},
            {"name": "Den store PP", "status": "I bruk", "bilde": "images/pp.jpg"},
            {"name": "Den store PP", "status": "I bruk", "bilde": "images/pp.jpg"},
            {"name": "Den store PP", "status": "I bruk", "bilde": "images/pp.jpg"},
            {"name": "Den store PP", "status": "I bruk", "bilde": "images/pp.jpg"},
        ]

        for pp in PPs_list:
            grid = GridLayout(cols=2, rows=2)
            grid_scheme.add_widget(grid)

            grid_elements = [
                Label(text=f"Navn: {pp['name']}"),
                Label(text=f"Status: {pp['status']}"),
                AsyncImage(
                    source='https://g.acdn.no/obscura/API/dynamic/r1/nadp/tr_1500_2000_s_f/0000/2019/09/16/3423846276/1/original/10099832.jpg?chk=7ABCCD'
                )
            ]

            see_detail_b = Button(text='Se detaljert', size=(1, 1))
            # needs bind to detailed view | FIXED 22/10 - Mathias
            see_detail_b.bind(on_press=lambda instance: self.switch_scene(2))

            grid_elements.append(see_detail_b)

            for e in grid_elements:
                grid.add_widget(e)

    def _create_detailedPP_owner_scene(self):
        self.orientation = "vertical"

        back_button = Button(text='Cancel', size=(100, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(0))
        self.add_widget(back_button)

        grid_scheme = GridLayout(cols=2, rows=7)
        self.add_widget(grid_scheme)

        for l in Gui.FIELDS:
            label = Label(text=l)
            grid_scheme.add_widget(label)
            if l == 'Bilde:':
                image = AsyncImage(
                    source='https://g.acdn.no/obscura/API/dynamic/r1/nadp/tr_1500_2000_s_f/0000/2019/09/16/3423846276/1/original/10099832.jpg?chk=7ABCCD')
                grid_scheme.add_widget(image)
            else:
                label2 = Label(text='eksempel detaljer')
                grid_scheme.add_widget(label2)

        edit_button = Button(text='Edit parking spot', size=(150, 40), size_hint=(None, None))
        edit_button.bind(on_press=lambda instance: self.switch_scene(1))
        self.add_widget(edit_button)

    def _create_detailedPP_renter_scene(self, ParkingPlaceID):
        self._clear_scene()
        self.orientation = "vertical"

        back_button = Button(text='Cancel', size=(100, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(4))
        self.add_widget(back_button)

        grid_scheme = GridLayout(cols=2, rows=7)
        self.add_widget(grid_scheme)

        currentParkingPlace = self.controller.get_pp_from_repo(ParkingPlaceID)

        grid_scheme.add_widget(Label(text="Navn på plassen"))
        grid_scheme.add_widget(Label(text=currentParkingPlace.name))

        grid_scheme.add_widget(Label(text="Adresse"))
        grid_scheme.add_widget(Label(text=currentParkingPlace.address))

        grid_scheme.add_widget(Label(text="Postkode"))
        grid_scheme.add_widget(Label(text=str(currentParkingPlace.zip_code)))

        grid_scheme.add_widget(Label(text="Antall plasser tilgjengelig"))
        grid_scheme.add_widget(Label(text=str(currentParkingPlace.number_of_places)))

        grid_scheme.add_widget(Label(text="Pris per time"))
        grid_scheme.add_widget(Label(text=str(currentParkingPlace.price_pr_hour) + " nok."))

        grid_scheme.add_widget(Label(text="Bilde av plassen (placeholder)"))
        grid_scheme.add_widget(AsyncImage(source=currentParkingPlace.picture))

        grid_scheme.add_widget(Label(text="Om parkeringsplassen"))
        grid_scheme.add_widget(Label(text=currentParkingPlace.details))

        confirm_button = Button(text='Confirm', size=(100, 40), size_hint=(None, None))
        confirm_button.bind(on_press=lambda instance: self.switch_scene(4))
        self.add_widget(confirm_button)

    def _show_available_and_active_parkings_scene(self):
        self.orientation = "vertical"

        grid_scheme = GridLayout(cols=1)
        self.add_widget(grid_scheme)

        back_button = Button(text='Main Menu',size=(250, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(5))
        grid_scheme.add_widget(back_button)

        l = Button(text='Aktive parkeringer:',size=(100, 40), size_hint=(1, None), background_color=(0.5,0.5,0.8,0.8), pos_hint={"top": 1})
        grid_scheme.add_widget(l)

        # PPs_list = FIKSE HVILKEN BACKEND SOM SKAL HIT

        PPs_list = [
            {"name": "Den opptatte PP","address": "Parkveien 1", "status": "Aktiv  (startet 15:23)"},
        ]

        for pp in PPs_list:
            grid = GridLayout(cols=4)
            grid_scheme.add_widget(grid)

            stopp_button = Button(text='STOPP', size_hint=(.4, .8), background_color=(1.0, 0.0, 0.0, 1.0))
            stopp_button.bind(on_press=lambda instance: self.switch_scene(5))

            grid_elements = [
                Label(text=f"Navn: {pp['name']}"),
                Label(text=f"Adresse: {pp['address']}"),
                Label(text=f"Status: {pp['status']}"),
                stopp_button
            ]

            for e in grid_elements:
                grid.add_widget(e)

        l = Button(text='Ledige parkeringer:', size=(100, 40), size_hint=(1, None), background_color=(0.5, 0.5, 0.8, 0.8),pos_hint={"top": 1})
        grid_scheme.add_widget(l)

        for pp in self.PPs_list:
            grid = GridLayout(cols=5)
            grid_scheme.add_widget(grid)
            lei_button = Button(text='      Lei \n Parkering', size_hint=(.55, 1), background_color=(129 / 255, 205 / 255, 48 / 255, 1.0))
            lei_button.bind(on_press=lambda instance, parkingId=pp.id: self._create_detailedPP_renter_scene(parkingId))

            grid_elements = [
                Label(text=f"Navn: {pp.name}"),
                Label(text=f"Adresse: {pp.address}"),
                Label(text=f"Pris: {pp.price_pr_hour}"),
                AsyncImage(
                    source = 'http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg'
                ),
                lei_button
            ]

            for e in grid_elements:
                grid.add_widget(e)

    def _main_menu_scene(self):
        self.orientation = "vertical"

        grid_scheme = GridLayout(cols=1, rows=3, padding=250, spacing=40)
        self.add_widget(grid_scheme)

        opt1_button = Button(text='Leier', size_hint=(.2, 1))
        opt1_button.bind(on_press=lambda instance: self.switch_scene(4))
        grid_scheme.add_widget(opt1_button)

        opt2_button = Button(text='Utleier', size_hint=(.2, 1))
        opt2_button.bind(on_press=lambda instance: self.switch_scene(0))
        grid_scheme.add_widget(opt2_button)

        opt3_button = Button(text='Min Profil', size_hint=(.2, 1))
        opt3_button.bind(on_press=lambda instance: self.switch_scene(6))
        grid_scheme.add_widget(opt3_button)

    def _my_profile_scene(self):
        self.orientation = "vertical"

        l = Label(text='DENNE SIDEN ER IKKE FERDIG ENDA, OG ER UNDER UTVIKLING')
        self.add_widget(l)

        opt1_button = Button(text='Main Menu', size=(200, 50), size_hint=(None, None))
        opt1_button.bind(on_press=lambda instance: self.switch_scene(5))
        self.add_widget(opt1_button)




