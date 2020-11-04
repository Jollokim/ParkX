from parkx_kode.model.Parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        self.parkingPlaces = []

        self.addPlaceholderPlaces()

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, id, name, address, zip_code, number_of_places, price_pr_hour, picture, details):
        new_pp = Parkingplace(id, name, address, zip_code, number_of_places, price_pr_hour, picture, details)

        print(new_pp.toString())
        self.parkingPlaces.append(new_pp)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp

    # TODO: needs double start for p_dict
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

    def addPlaceholderPlaces(self):
        pPlace1 = {
            "id": 0,
            "name": "Hjembua",
            "address": "Hjørneveien 3",
            "zip_code": 1882,
            "number_of_places": 4,
            "price_pr_hour": 8234,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger i hjørnet",
            # "available": True
        }

        pPlace2 = {
            "id": 1,
            "name": "Trollhullet",
            "address": "Trolleren 10",
            "zip_code": 7123,
            "number_of_places": 2,
            "price_pr_hour": 42,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Troll kan trolle...",
            # "available": True
        }

        pPlace3 = {
            "id": 2,
            "name": "Hullet",
            "address": "Storgata 5",
            "zip_code": 8329,
            "number_of_places": 11,
            "price_pr_hour": 89,
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger under bakken",
            # "available": False
        }

        self.addNewParkingPlace(**pPlace1)

        self.addNewParkingPlace(**pPlace2)

        self.addNewParkingPlace(**pPlace3)
