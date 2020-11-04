import datetime

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

    def change_pp_status(self, id):
        obj = self.repository.getPP(id)

        if obj.available:
            obj.available = False
            obj.parkingStarted = datetime.datetime.now().strftime("%H:%M:%S")
        else:
            obj.available = True

    def calc_parking_price(self, parking_id, parkingStopped):

        parkingPlace = self.repository.getPP(parking_id)

        FMT = '%H:%M:%S'
        parkedTimeDelta = datetime.datetime.strptime(parkingStopped, FMT) \
               - datetime.datetime.strptime(parkingPlace.parkingStarted, FMT)

        ParkedTimeSec = parkedTimeDelta.total_seconds()
        ParkedTimeHour = (ParkedTimeSec/3600)

        totalPrice = ParkedTimeHour * parkingPlace.price_pr_hour
        totalPriceTwoDec = str("{:.2f}".format(totalPrice))
        return totalPriceTwoDec

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def addPlaceholderPlaces(self):
        pPlace1 = {
            "name": "Hjembua",
            "address": "Hjørneveien 3",
            "zip_code": 1882,
            "number_of_places": 1,
            "price_pr_hour": 3600,              #priser er kunstig høye for å rask se resultat i programmet
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger i hjørnet",
            "available": False
        }

        pPlace2 = {
            "name": "Trollhullet",
            "address": "Trolleren 10",
            "zip_code": 7123,
            "number_of_places": 1,
            "price_pr_hour": 8200,      #priser er kunstig høye for å rask se resultat i programmet
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Troll kan trolle...",
            "available": True
        }

        pPlace3 = {
            "name": "Hullet",
            "address": "Storgata 5",
            "zip_code": 8329,
            "number_of_places": 1,
            "price_pr_hour": 3500,          #priser er kunstig høye for å rask se resultat i programmet
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger under bakken",
            "available": True
        }
        self.add_parking_place_to_repo(pPlace1)
        self.add_parking_place_to_repo(pPlace2)
        self.add_parking_place_to_repo(pPlace3)
