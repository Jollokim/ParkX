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
