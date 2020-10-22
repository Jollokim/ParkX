class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def increaseCounter(self):
        self.counter += 1

    def addNewParkingPlace(self, p_data):
        print(p_data)
