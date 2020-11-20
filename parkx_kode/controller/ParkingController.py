from parkx_kode.model import Payment


class ParkingController:
    def __init__(self, gui, payment, repository,):
        self.payment = payment
        self.gui = gui
        self.repository = repository
        self.counter = 4

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place_to_repo(self, p_dict):
        p_dict["id"] = self.counter

        self.increaseCounter()
        p_dict = self.validateUserInput(p_dict)
        self.repository.addNewParkingPlace(**p_dict)

    def remove_parkingplace(self, id):
        self.repository.removeParkingPlace(id)

    def get_pp_from_repo(self, id):
        return self.repository.getPP(id)

    def get_all_pp_from_list(self):
        return self.repository.getAllParkingPlaces()

    def change_pp(self, p_dict, id):
        p_dict["id"] = id
        p_dict = self.validateUserInput(p_dict)
        self.repository.changePP(p_dict)

    def change_pp_status(self, id):
        self.repository.updateParkingPlaceStatus(id)

    def calc_parking_price(self, id, parkingStopped):
        calculatedPrice = self.repository.calculatePriceForParkingPeriod(id, parkingStopped)
        return calculatedPrice

    def validateUserInput(self, p_dict):
        try:
            p_dict["id"] = int(p_dict["id"])
            p_dict["name"] = str(p_dict["name"])
            p_dict["address"] = str(p_dict["address"])
            p_dict["zip_code"] = str(p_dict["zip_code"])
            p_dict["number_of_places"] = int(p_dict["number_of_places"])
            if isinstance(p_dict["price_pr_hour"], str):
                p_dict["price_pr_hour"] = p_dict["price_pr_hour"].replace(",", ".")
            p_dict["price_pr_hour"] = float(p_dict["price_pr_hour"])
            p_dict["picture"] = str(p_dict["picture"])
            p_dict["details"] = str(p_dict["details"])
            return p_dict
        except ValueError:
            raise ValueError

    def reset_parking_started(self, parking_id):
        self.repository.getPP(parking_id).reset_parkingStarted()

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def add_new_payment(self, name, parkingstarted, parkingStopped, price_to_pay):
        self.payment.add_new_payment(name, parkingstarted, parkingStopped, price_to_pay)

    def get_all_payments(self):
        return self.payment.get_all_payments()

    def pay_all_payments(self):
        self.payment.pay_all_payments()

    def change_accepted_payment_details(self, buttonValueBool):
        self.payment.change_accepted_payment_details(buttonValueBool)

    def check_accepted_payment_details(self):
        return self.payment.check_accepted_payment_details()
