from parkx_kode.model.Parkingplace import Parkingplace
from parkx_kode.repository.ListRepository import ListRepository


class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place_to_repo(self, p_dict):
        p_dict["id"] = self.counter

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

        p_dict["id"] = id

        self.repository.addNewParkingPlace(p_dict)


    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def addPlaceholderPlaces(self):
        pPlace1 = {
            "id": "1",
            "name": "Hjembua",
            "address": "Hjørneveien 3",
            "zip_code": 1882,
            "number_of_places": 4,
            "price_pr_hour": 150,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger i hjørnet",
            "available": True
        }

        pPlace2 = {
            "id": "2",
            "name": "Trollhullet",
            "address": "Trolleren 10",
            "zip_code": 7123,
            "number_of_places": 2,
            "price_pr_hour": 42,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Troll kan trolle...",
            "available": True
        }

        pPlace3 = {
            "id": "3",
            "name": "Hullet",
            "address": "Storgata 5",
            "zip_code": 8329,
            "number_of_places": 11,
            "price_pr_hour": 89,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger under bakken",
            "available": False
        }
        self.add_parking_place_to_repo(pPlace1)
        self.add_parking_place_to_repo(pPlace2)
        self.add_parking_place_to_repo(pPlace3)
