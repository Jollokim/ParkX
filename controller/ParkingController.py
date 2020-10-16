class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def getCounter(self):
        return self.counter

    def increaseCoutner(self):
        self.counter += 1
