import datetime

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
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
    ENG_FIELDS = [
        "name",
        "address",
        "zip_code",
        "number_of_places",
        "price_pr_hour",
        "picture",
        "details"
    ]

    def __init__(self, controller, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.controller = controller

        self.PPs_list = controller.get_all_pp_from_list()

        self.text_fields = []

        self.SCENES = [
            self._create_my_PPs_scene,
            self._create_new_PP_scene,
            self._create_detailedPP_owner_scene,
            self._create_detailedPP_renter_scene,
            self._show_available_and_active_parkings_scene,
            self._main_menu_scene,
            self._my_profile_scene
        ]

        self.SCENES[0]()

    def _create_new_PP_scene(self, ParkingPlaceID=None):
        self._clear_scene()
        self.orientation = "vertical"

        self.spacing = [20, 20]

        back_button = Button(text='Avbryt', size=(100, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(0))
        self.add_widget(back_button)

        grid_scheme = GridLayout(cols=2, rows=7)
        self.add_widget(grid_scheme)

        for i in range(len(Gui.FIELDS)):
            label = Label(text=Gui.FIELDS[i])
            text_input = TextInput(text='', multiline=True)

            self.text_fields.append(text_input)
            grid_scheme.add_widget(label)
            grid_scheme.add_widget(text_input)

        if ParkingPlaceID is not None:
            pp = self.controller.get_pp_from_repo(ParkingPlaceID)
            ppDict = pp.__dict__
            ppAttributeList = list(ppDict.values())[1:-2]

            for i in range(len(self.text_fields)):
                self.text_fields[i].text = str(ppAttributeList[i])

        if ParkingPlaceID is not None:
            insert_pp_button = Button(text='Endre', size=(100, 40), size_hint=(None, None))
            insert_pp_button.bind(
                on_press=lambda instance: self.insert_pp_button_handler(instance, True, ParkingPlaceID))
        else:
            insert_pp_button = Button(text='Legg til', size=(100, 40), size_hint=(None, None))
            insert_pp_button.bind(on_press=self.insert_pp_button_handler)
        self.add_widget(insert_pp_button)

    def insert_pp_button_handler(self, instance, changing=False, ParkingPlaceID=None):
        try:
            data_dict = {}

            for i in range(len(self.text_fields)):
                data_dict[Gui.ENG_FIELDS[i]] = self.text_fields[i].text

            if changing == True and ParkingPlaceID != None:
                self.controller.change_pp(data_dict, ParkingPlaceID)
            else:
                self.controller.add_parking_place_to_repo(data_dict)
        except ValueError:
            newPopup = Popup(title='An error occured', content=Label(text='An error occured when processing data, check if correct data was given in the fields'))
            newPopup.open()
            self._create_new_PP_scene(ParkingPlaceID)

        self.switch_scene(0)

    def _clear_scene(self):
        self.clear_widgets()
        self.text_fields.clear()

    def switch_scene(self, n_scene):
        self._clear_scene()
        self.SCENES[n_scene]()

    def _create_my_PPs_scene(self):
        self.orientation = "vertical"

        self.spacing = [20, 20]

        button_box = BoxLayout(orientation="horizontal", spacing=0, size_hint=(1, 0.1))
        self.add_widget(button_box)

        back_button = Button(text='Hovedmeny', size=(100, 40), size_hint=(.1, 0), pos_hint={"top": 1})
        back_button.bind(on_press=lambda instance: self.switch_scene(5))
        button_box.add_widget(back_button)

        go_leggInn_button = Button(text='Legg til parkeringsplass', size=(100, 40), size_hint=(.1, 0),
                                   pos_hint={"top": 1})
        go_leggInn_button.bind(on_press=lambda instance: self.switch_scene(1))

        button_box.add_widget(go_leggInn_button)

        pps_list = self.controller.get_all_pp_from_list()

        grid_scheme = GridLayout(cols=1, rows=len(pps_list))
        self.add_widget(grid_scheme)

        for pp in pps_list:
            grid = GridLayout(cols=2, rows=2)
            grid_scheme.add_widget(grid)

            status = None

            if pp.parkingStarted != None:
                status = "I bruk"
            else:
                status = "Ikke i bruk"

            grid_elements = [
                Label(text=f"Navn: {pp.name}"),
                Label(text=f"Status: {status}"),
                AsyncImage(
                    source=pp.picture
                )
            ]

            see_detail_b = Button(text='Se detaljert', size=(1, 1))
            # needs bind to detailed view | FIXED 22/10 - Mathias
            see_detail_b.bind(on_press=lambda instance, id=pp.id:
            self._create_detailedPP_owner_scene(id))

            grid_elements.append(see_detail_b)

            for e in grid_elements:
                grid.add_widget(e)

    def delete_PP_button_handler(self, ParkingPlaceID):
        self.controller.remove_parkingplace(ParkingPlaceID)
        self.switch_scene(0)

    def _create_detailedPP_owner_scene(self, ParkingPlaceID):
        self._clear_scene()

        self.orientation = "vertical"

        button_box = BoxLayout(orientation="horizontal", spacing=0, size_hint=(1, 0.1))
        self.add_widget(button_box)

        back_button = Button(text='Tilbake', size=(100, 40), size_hint=(.1, 0), pos_hint={"top": 1})
        back_button.bind(on_press=lambda instance: self.switch_scene(0))
        button_box.add_widget(back_button)

        delete_button = Button(text='Slett denne Parkeringsplassen', size=(100, 40), size_hint=(.1, 0),
                               pos_hint={"top": 1})
        delete_button.bind(on_press=lambda instance: self.delete_PP_button_handler(ParkingPlaceID))

        button_box.add_widget(delete_button)

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
        grid_scheme.add_widget(Label(text=str(currentParkingPlace.price_pr_hour) + " kr/t"))

        grid_scheme.add_widget(Label(text="Bilde av plassen"))
        grid_scheme.add_widget(AsyncImage(source=currentParkingPlace.picture))

        grid_scheme.add_widget(Label(text="Om parkeringsplassen"))
        grid_scheme.add_widget(Label(text=currentParkingPlace.details))

        confirm_button = Button(text='Endre', size=(130, 60), background_color=(129 / 255, 205 / 255, 48 / 255, 1.0),
                                size_hint=(None, None))
        confirm_button.bind(on_press=lambda instance: self._create_new_PP_scene(ParkingPlaceID))
        self.add_widget(confirm_button)

    def _create_detailedPP_renter_scene(self, ParkingPlaceID):
        self._clear_scene()
        self.orientation = "vertical"

        back_button = Button(text='Avbryt', size=(100, 40), size_hint=(None, None))
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
        grid_scheme.add_widget(Label(text=str(currentParkingPlace.price_pr_hour) + " kr/t"))

        grid_scheme.add_widget(Label(text="Bilde av plassen"))
        grid_scheme.add_widget(AsyncImage(source=currentParkingPlace.picture))

        grid_scheme.add_widget(Label(text="Om parkeringsplassen"))
        grid_scheme.add_widget(Label(text=currentParkingPlace.details))

        confirm_button = Button(text='Bekreft', size=(130, 60), background_color=(129 / 255, 205 / 255, 48 / 255, 1.0),
                                size_hint=(None, None))
        confirm_button.bind(on_press=lambda instance: self.change_parking_status(ParkingPlaceID))
        self.add_widget(confirm_button)

    def popup_ended_parking(self, parking_id):

        layout = GridLayout(cols=1, rows=2, padding=10)

        popup = Popup(title='Parkering stanset', content=layout, size_hint=(None, None), size=(400, 300))
        popup.open()

        parkid = self.controller.get_pp_from_repo(parking_id)

        parkingStopped = datetime.datetime.now().strftime("%H:%M:%S")

        total_parking_price = self.controller.calc_parking_price(parking_id, parkingStopped)

        l = Label(
            text='Din parkering med navn ' + parkid.name + ' er nå stanset: \n\n Adresse: ' + parkid.address + '\n Parkering startet: ' + parkid.parkingStarted + '\n Parkering stoppet: ' + parkingStopped + '\n Totalpris: ' + total_parking_price + 'kr')

        layout.add_widget(l)

        closeButton = Button(text='Lukk', size_hint=(None, None), size=(350, 50))

        closeButton.bind(on_press=popup.dismiss)
        layout.add_widget(closeButton)

    def change_parking_status(self, parking_id):

        self.controller.change_pp_status(parking_id)
        self.switch_scene(4)

    def _show_available_and_active_parkings_scene(self):
        self.orientation = "vertical"

        grid_scheme = GridLayout(cols=1)
        self.add_widget(grid_scheme)

        back_button = Button(text='Hovedmeny', size=(250, 40), size_hint=(None, None))
        back_button.bind(on_press=lambda instance: self.switch_scene(5))
        grid_scheme.add_widget(back_button)

        l = Button(text='Aktive parkeringer:', size=(100, 40), size_hint=(1, None),
                   background_color=(0.5, 0.5, 0.8, 0.8), pos_hint={"top": 1})
        grid_scheme.add_widget(l)

        for pp in self.PPs_list:
            if not pp.available:
                grid = GridLayout(cols=4)
                grid_scheme.add_widget(grid)

                stop_button = Button(text='STOPP', size_hint=(.4, .8), background_color=(1.0, 0.0, 0.0, 1.0))
                stop_button.bind(on_press=lambda instance, parkingId=pp.id: self.change_parking_status(parkingId))
                stop_button.bind(on_press=lambda instance, parkingId=pp.id: self.popup_ended_parking(parkingId))

                grid_elements = [
                    Label(text=f"Navn: {pp.name}"),
                    Label(text=f"Adresse: {pp.address}"),
                    Label(text=f"Parkering startet: {pp.parkingStarted}"),
                    stop_button
                ]

                for e in grid_elements:
                    grid.add_widget(e)

        l = Button(text='Ledige parkeringer:', size=(100, 40), size_hint=(1, None),
                   background_color=(0.5, 0.5, 0.8, 0.8), pos_hint={"top": 1})
        grid_scheme.add_widget(l)

        for pp in self.PPs_list:

            if pp.available:
                grid = GridLayout(cols=5)
                grid_scheme.add_widget(grid)
                lei_button = Button(text='      Lei \n Parkering', size_hint=(.55, 1),
                                    background_color=(129 / 255, 205 / 255, 48 / 255, 1.0))
                lei_button.bind(
                    on_press=lambda instance, parkingId=pp.id: self._create_detailedPP_renter_scene(parkingId))

                grid_elements = [
                    Label(text=f"Navn: {pp.name}"),
                    Label(text=f"Adresse: {pp.address}"),
                    Label(text=f"Pris: {pp.price_pr_hour} kr/t"),
                    AsyncImage(
                        source='http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg'
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

        opt1_button = Button(text='Hovedmeny', size=(200, 50), size_hint=(None, None))
        opt1_button.bind(on_press=lambda instance: self.switch_scene(5))
        self.add_widget(opt1_button)
