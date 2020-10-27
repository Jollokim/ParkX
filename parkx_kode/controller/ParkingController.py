from parkx_kode.model.parkingplace import parkingplace


class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def increaseCounter(self):
        self.counter += 1

    def add_parking_place(self, p_data):
        pp = parkingplace(None, p_data["Navn"], p_data["Adresse"], p_data["PostAdr"], p_data["Antall"], p_data["Pris"], p_data["Bilde"], p_data["Detaljer"])

        return pp
