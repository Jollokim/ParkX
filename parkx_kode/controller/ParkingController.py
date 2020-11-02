from parkx_kode.model.parkingplace import Parkingplace
from parkx_kode.repository.ListRepository import ListRepository


class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0
        self.addPlaceholderPlaces()

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place_to_repo(self, p_dict):
        p_dict["ID"] = self.counter

        self.increaseCounter()

        self.repository.addNewParkingPlace(p_dict)

    def remove_parkingplace(self, id):
        self.repository.removeParkingPlace(id)

    def get_pp_from_repo(self, id):
        return self.repository.getPP(id)

    def get_all_pp_from_list(self):
        return self.repository.getAllParkingPlaces()

    def change_pp(self, id, p_dict):
        self.remove_parkingplace(id)

        p_dict["ID"] = id

        self.repository.addNewParkingPlace(p_dict)


    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def addPlaceholderPlaces(self):
        pPlace1 = {
            "Navn": "Hjembua",
            "Adresse": "Hjørneveien 3",
            "PostAdr": 1882,
            "Antall": 4,
            "Pris": 150,
            "Bilde": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "Detaljer": "Ligger i hjørnet"
        }

        pPlace2 = {
            "Navn": "Trollhullet",
            "Adresse": "Trolleren 10",
            "PostAdr": 7123,
            "Antall": 2,
            "Pris": 42,
            "Bilde": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "Detaljer": "Troll kan trolle..."
        }

        pPlace3 = {
            "Navn": "Hullet",
            "Adresse": "Storgata 5",
            "PostAdr": 8329,
            "Antall": 11,
            "Pris": 89,
            "Bilde": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "Detaljer": "Ligger under bakken"
        }
        self.add_parking_place_to_repo(pPlace1)
        self.add_parking_place_to_repo(pPlace2)
        self.add_parking_place_to_repo(pPlace3)
