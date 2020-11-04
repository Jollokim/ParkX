import datetime

from parkx_kode.model.Parkingplace import Parkingplace
from parkx_kode.repository.ListRepository import ListRepository


class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 4

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place_to_repo(self, p_dict):
        p_dict["id"] = self.counter

        self.increaseCounter()

        self.repository.addNewParkingPlace(**p_dict)

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

