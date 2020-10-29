class ListRepository:
    def __init__(self):
        self.parkingPlaces = []

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, pPlace):
        self.parkingPlaces.append(pPlace)

    def removeParkingPlace(self, pPlace):
        self.parkingPlaces.remove(pPlace)