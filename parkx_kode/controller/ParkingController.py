from parkx_kode.model.parkingplace import Parkingplace
from parkx_kode.repository.ListRepository import ListRepository

class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place_to_repo(self, p_dict):
        p_dict["ID"] = self.counter

        self.increaseCounter()

        self.repository.addNewParkingPlace(p_dict)

        return p_dict

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")
