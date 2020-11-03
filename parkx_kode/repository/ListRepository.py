from parkx_kode.model.Parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        self.parkingPlaces = []

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, p_dict):
        new_pp = Parkingplace(p_dict["ID"], p_dict["Navn"], p_dict["Adresse"],
                              p_dict["PostAdr"], p_dict["Antall"],
                              p_dict["Pris"], p_dict["Bilde"],
                              p_dict["Detaljer"])

        self.parkingPlaces.append(new_pp)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp

    def changePP(self, id, p_dict):
        pp = self.getPP(id)

        pp.name = p_dict["Name"]
        pp.address = p_dict["Adresse"]
        pp.zip_code = p_dict["PostAdr"]
        pp.number_of_place = p_dict["Antall"]
        pp.price_pr_hour = p_dict["Pris"]
        pp.picture = p_dict["Bilde"]
        pp.details = p_dict["Detaljer"]
        pp.available = p_dict["Available"]
