from parkx_kode.model.parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        self.parkingPlaces = []

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, p_dict):
        new_pp = Parkingplace(p_dict["ID"], p_dict["Navn"], p_dict["Adresse"], p_dict["PostAdr"], p_dict["Antall"],
                              p_dict["Pris"], p_dict["Bilde"], p_dict["Detaljer"])

        self.parkingPlaces.append(new_pp)

        print(self.parkingPlaces)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp
