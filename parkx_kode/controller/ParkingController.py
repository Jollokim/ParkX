
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
        self.validateUserInput(p_dict)
        self.repository.addNewParkingPlace(**p_dict)

    def remove_parkingplace(self, id):
        self.repository.removeParkingPlace(id)

    def get_pp_from_repo(self, id):
        return self.repository.getPP(id)

    def get_all_pp_from_list(self):
        return self.repository.getAllParkingPlaces()

    def change_pp(self, p_dict, id):
        p_dict["id"] = id
        self.validateUserInput(p_dict)
        self.repository.changePP(p_dict)

    def change_pp_status(self, id):
        self.repository.updateParkingPlaceStatus(id)

    def calc_parking_price(self, id, parkingStopped):
        calculatedPrice = self.repository.calculatePriceForParkingPeriod(id, parkingStopped)
        return calculatedPrice

    def validateUserInput(self, p_dict):
        try:
            int(p_dict["id"])
            str(p_dict["name"])
            str(p_dict["address"])
            str(p_dict["zip_code"])
            int(p_dict["number_of_places"])
            int(p_dict["price_pr_hour"])
            str(p_dict["picture"])
            str(p_dict["details"])
        except ValueError:
            raise ValueError

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

