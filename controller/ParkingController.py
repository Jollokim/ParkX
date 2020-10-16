class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")
