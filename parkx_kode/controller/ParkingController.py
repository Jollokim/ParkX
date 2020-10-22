from model.parkingplace import *

class ParkingController:
    def __init__(self, gui, repository):
        self.gui = gui
        self.repository = repository
        self.counter = 0

    def toString(self):
        return str(f"Gui: {self.gui} Repository: {self.repository}")

    def increaseCounter(self):
        self.counter += 1

    def addNewParkingPlace(self, id, name, address, zip_code, number_of_places, price_pr_hour, picture, details):
       newSpace = parkingplace(id, name, address, zip_code, number_of_places, price_pr_hour, picture, details)
       newSpace.Repository.addNewParkingPlaceToRepository

    def getAExistingParkingPlace(self, parkingPlaceName):
        Repository.getAParkingPlace(parkingPlaceName)

    def getAllExistingParkingPlaces(self):
        Repository.getAllParkingPlaces()



