from parkx_kode.model.Parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        self.parkingPlaces = []

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, p_dict):

        if not p_dict["available"] == False:
            p_dict["available"] = True

        new_pp = Parkingplace(p_dict["id"], p_dict["name"], p_dict["address"],
                              p_dict["zip_code"], p_dict["number_of_places"],
                              p_dict["price_pr_hour"], p_dict["picture"],
                              p_dict["details"], p_dict["available"])

        self.parkingPlaces.append(new_pp)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp

    def changePP(self, id, p_dict):
        pp = self.getPP(id)

        pp.name = p_dict["name"]
        pp.address = p_dict["address"]
        pp.zip_code = p_dict["zip_code"]
        pp.number_of_place = p_dict["number_of_places"]
        pp.price_pr_hour = p_dict["price_pr_hour"]
        pp.picture = p_dict["picture"]
        pp.details = p_dict["details"]
        pp.available = p_dict["available"]
